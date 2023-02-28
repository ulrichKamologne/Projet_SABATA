import cv2
import numpy as np

cap = cv2.VideoCapture(0)
stop_cascade = cv2.CascadeClassifier('Stop_classificateur.xml')

while True:
    ret, img = cap.read()
    img = cv2.resize(img,(340, 220))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    panneaux = stop_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in panneaux:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        panneau = img[y:y+h, x:x+w]
        cv2.imshow('panneau STOP', panneau)
    cv2.imshow('img', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cap.release() cv2.destroyAllWindows()

from sys import argv, exit
from time import sleep
import cv2
from kafka import KafkaProducer


class kafkaVideoStreaming():
    def __init__ (self, bootstrap_servers, topic, videoFile, client_id, batch_size=65536, frq=0.001):
        self.videoFile = videoFile
        self.topicKey = str(videoFile)
        self.topic = topic
        self.batch_size = batch_size
        self.client_id = client_id
        self.bootstrap_servers = bootstrap_servers
        self.frq = frq

    def setProducer (self):
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            api_version=(0, 10, 1),
            client_id=self.client_id,
            acks=1,
            value_serializer=None,
            key_serializer=str.encode,
            batch_size=self.batch_size,
            compression_type='gzip',
            linger_ms=0,
            buffer_memory=67108864,
            max_request_size=1048576,
            max_in_flight_requests_per_connection=1,
            retries=1,
        )

    def reportCallback (self, record_metadata):
        print("Topic Record Metadata: ", record_metadata.topic)
        print("Parition Record Metadata: ", record_metadata.partition)
        print("Offset Record Metatada: ", record_metadata.offset)

    def errCallback (self, excp):
        print('Errback', excp)

    def publishFrames (self, payload):
        self.producer.send(
            topic=self.topic, key=self.topicKey, value=payload
        ).add_callback(
            self.reportCallback
        ).add_errback(
            self.errCallback
        )

    def run (self):
        try:
            print("Opening file %s" % self.videoFile)
            __VIDEO_FILE = cv2.VideoCapture(self.videoFile)
        except:
            raise

        self.setProducer()

        print(
            "Publishing: %{v}\n\
            \tBatch Size: {b},\n\
            \tSleep ({t}) \n\
            \tTarget Topic: {t} \n\
            \tHost: {h}".format(
                v=self.topicKey,
                b=self.batch_size,
                t=self.topic,
                h=self.bootstrap_servers
            )
        )

        self.keep_processing = True
        try:
            while (__VIDEO_FILE.isOpened()) and self.keep_processing:
                readStat, frame = __VIDEO_FILE.read()

                if not readStat:
                    self.keep_processing = False

                ret, buffer = cv2.imencode('.jpg', frame)
                self.publishFrames(buffer.tostring())

                sleep(self.frq)

            if self.keep_processing:
                print('Finished processing video %s' % self.topicKey)
            else:
                print("Error while reading %s" % self.topicKey)

            __VIDEO_FILE.release()
        except KeyboardInterrupt:
            __VIDEO_FILE.release()
            print("Keyboard interrupt was detected. Exiting...")


if __name__ == "__main__":
    videoStream = kafkaVideoStreaming(
        bootstrap_servers='localhost:9092',
        topic='KafkaVideoStream',
        videoFile=argv[1],
        client_id='KafkaVideoStreamClient',
    )
    videoStream.run()

    from kafka import KafkaConsumer
    from time import sleep
    import cv2
    import numpy as np
    from queue import Queue
    from threading import Thread
    from threading import Event


    class kafkaVideoView():
        def __init__ (self, bootstrap_servers, topic, client_id, group_id, poll=500, frq=0.01):
            self.topic = topic
            self.client_id = client_id
            self.group_id = group_id
            self.bootstrap_servers = bootstrap_servers
            self.poll = poll
            self.frq = frq

        def setConsumer (self):
            self.consumer = KafkaConsumer(
                self.topic,
                bootstrap_servers=self.bootstrap_servers.split(','),
                fetch_max_bytes=52428800,
                fetch_max_wait_ms=1000,
                fetch_min_bytes=1,
                max_partition_fetch_bytes=1048576,
                value_deserializer=None,
                key_deserializer=None,
                max_in_flight_requests_per_connection=10,
                client_id=self.client_id,
                group_id=self.group_id,
                auto_offset_reset='earliest',
                max_poll_records=self.poll,
                max_poll_interval_ms=300000,
                heartbeat_interval_ms=3000,
                session_timeout_ms=10000,
                enable_auto_commit=True,
                auto_commit_interval_ms=5000,
                reconnect_backoff_ms=50,
                reconnect_backoff_max_ms=500,
                request_timeout_ms=305000,
                receive_buffer_bytes=32768,
            )

        def playStream (self, queue):
            while self.keepPlaying:
                try:
                    msg = queue.get(block=True, timeout=20)
                    self.queue_status = True
                except:
                    print("WARN: Timed out waiting for queue. Retrying...")
                    self.queue_status = False

                if self.queue_status:
                    nparr = np.frombuffer(msg, np.uint8)
                    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                    cv2.imshow('frame', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        self.keepConsuming = False
                        break

                    sleep(self.frq)

        def run (self):
            self.keepPlaying = True
            self.setConsumer()
            self.videoQueue = Queue()
            self.keepConsuming = True

            self.playerThread = Thread(target=self.playStream, args=(self.videoQueue,), daemon=False)
            self.playerThread.start()

            try:
                while self.keepConsuming:
                    payload = self.consumer.poll(self.poll)
                    for bucket in payload:
                        for msg in payload[bucket]:
                            self.videoQueue.put(msg.value)

            except KeyboardInterrupt:
                self.keepConsuming = False
                self.keepPlaying = False
                print("WARN: Keyboard Interrupt detected. Exiting...")

            self.playerThread.join()


    if __name__ == "__main__":
        streamVideoPlayer = kafkaVideoView(
            bootstrap_servers='localhost:9092',
            topic='KafkaVideoStream',
            client_id='KafkaVSClient',
            group_id='KafkaVideoStreamConsumer',
            poll=500,
            frq=0.025
        )

        streamVideoPlayer.run()