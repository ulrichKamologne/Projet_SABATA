import pyttsx3
#import pyPDF2

def voice(text):
    droid = pyttsx3.init()
    droid.setProperty("voice","fr")
    droid.say(text)
    droid.runAndWait()

# asistance panneau

def audio(id_name):
    if id_name == 1:
        voice('panneau stop a 50 metre')
        voice('veiller ralentire votre vehicule')
    if id_name == 2:
        voice('panneau limitation de vitesse a 50 metre')
        voice('veiller garder la vitesse de votre vehicue en desous de 30 kilometre par heur')
    if id_name == 3:
        voice('panneau limitation de vitesse a 50 metre')
        voice('veiller garder la vitesse de votre vehicue en desous de 50 kilometre par heur')
    if id_name == 4:
        voice('panneau limitation de vitesse a 50 metre')
        voice('veiller garder la vitesse de votre vehicue en desous de 90 kilometre par heur')
    if id_name == 5:
        voice('panneau annonce dun etablicement sclolaire a 50 metre')
        voice('veiller garder la vitesse de votre vehicue en desous de 30 kilometre par heur pour eviter de percuter un eleve')

#audio(5)