'''Pour mettre limage issue de la webcam dans une frame particulière en Python, vous pouvez utiliser
la bibliothèque Tkinter pour créer une interface graphique et afficher limage dans un widget `Label`.'''

'''
Voici un exemple de code qui utilise OpenCV pour récupérer les données de la webcam et Tkinter pour 
afficher limage dans un widget `Label` :
'''
import cv2
import customtkinter
from PIL import Image, ImageTk


# Ouvrir la webcam
cap = cv2.VideoCapture(0)

def update_image(image_label):
    # Lire une image de la webcam
    rec, frame=  cap.read()
    frame.configure()

    # Convertir l'image OpenCV en image Tkinter
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    # Afficher l'image dans le widget Label
    image_label.configure(image=image)
    image_label.image = image

    # Planifier la prochaine mise à jour de l'image
    image_label.after(10, update_image, image_label)

# Planifier la première mise à jour de l'image


def camera(parent):
    image_label = customtkinter.CTkLabel(parent, text='', anchor='center')
    image_label.grid(row=0, column=0, sticky='nsew')
    update_image(image_label)
    # image_label.after(10, update_image)
