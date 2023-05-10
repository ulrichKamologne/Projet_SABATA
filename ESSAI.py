import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Créer la fenêtre principale
root = tk.Tk()

# Créer un widget Label pour afficher l'image
image_label = tk.Label(root)
image_label.pack()

# Ouvrir la webcam
cap = cv2.VideoCapture(0)

def update_image():
    # Lire une image de la webcam
    ret, frame = cap.read()

    # Convertir l'image OpenCV en image Tkinter
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    image = ImageTk.PhotoImage(image)

    # Afficher l'image dans le widget Label
    image_label.configure(image=image)
    image_label.image = image

    # Planifier la prochaine mise à jour de l'image
    image_label.after(1, update_image)

# Planifier la première mise à jour de l'image
image_label.after(1, update_image)

# Démarrer la boucle principale de Tk
update_image()
root.mainloop()