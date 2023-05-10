#---------BIBLIOTHEQUES/MODULES---------
import folium
import webbrowser
from tkinter.messagebox import * # boîte de dialogue
from tkinter import *
import tkinter as tk

#----------FONCTIONS----------
# Fonction carte
def carte():
    # Récupération des données entrées
    nomlieu = nom.get()
    longitude = long.get()
    latitude = lat.get()
    cercle1 = per1.get()
    cercle2 = per2.get()
    # lieu = [46.548312, 3.287667]
    lieu = [longitude, latitude]
    # Création d'une carte
    carte= folium.Map(location=lieu,zoom_start=12)
    # Ajout marqueur avec légende, couleur
    folium.Marker(
        location=lieu,
        popup=nomlieu,
        icon=folium.Icon(color='green')
        ).add_to(carte)
    # Cercle de confinement en mètres (radius = 1000 pour 1 km)
    folium.Circle(lieu,radius = cercle1, fill=True, color='red' ).add_to(carte)
    folium.Circle(lieu,radius = cercle2, fill=True, color='orange' ).add_to(carte)
    # enregistrement et affichage de la carte
    nomcarte = nomlieu+'_'+cercle1+'_'+cercle2+'.html'
    carte.save(nomcarte)
    webbrowser.open(nomcarte)