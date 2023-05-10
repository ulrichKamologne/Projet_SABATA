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

#----------PROGRAMME PRINCIPAL----------

# Création de la fenêtre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Périmètres')
# Taille de la fenêtre
Mafenetre.geometry("460x220")
Mafenetre.configure(bg = 'orange')
tk.Label(Mafenetre, text = 'Périmètre(s) d'+"'"+'influence ',
bg = 'orange', font=("Arial", 12, "bold")).grid(row=0, column=1)

# widget Nom du Lieu
tk.Label(Mafenetre, text = 'Nom du Lieu ',
bg = 'orange', font=("Arial", 11)).grid(row=1)
nom = tk.Entry(Mafenetre, bg ='bisque', fg='blue', font=("Arial", 11))
nom.grid(row=1, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=1, column=2)
# widget Longitude
tk.Label(Mafenetre, text = 'Longitude ',
bg = 'orange', font=("Arial", 11)).grid(row=2)
long = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
long.grid(row=2, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=2, column=2)
# widget Latitude
tk.Label(Mafenetre, text = 'Latitude ',
bg = 'orange', font=("Arial", 11)).grid(row=3)
lat = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
lat.grid(row=3, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=3, column=2)

# widget Petit périmètre
tk.Label(Mafenetre, text = 'Petit Périmètre (en m) ',
bg = 'orange', font=("Arial", 11)).grid(row=4)
per1 = tk.Entry(Mafenetre, bg ='bisque', fg='red', font=("Arial", 11))
per1.grid(row=4, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=4, column=2)

# widget Grand périmètre
tk.Label(Mafenetre, text = 'Grand Périmètre (en m) ',
bg = 'orange', font=("Arial", 11)).grid(row=5)
per2 = tk.Entry(Mafenetre, bg ='bisque', fg='red', font=("Arial", 11))
per2.grid(row=5, column=1)
tk.Label(Mafenetre, text = 'Optionnel', bg = 'orange', font=("Arial", 11)).grid(row=5, column=2)

# widget bouton Valider
Valider = tk.Button(Mafenetre, text ='Valider', font=("Arial", 12, "bold"), command=carte)
Valider.grid(row=6, column=1, sticky=tk.W, pady=4)

# widget bouton Quitter
Quitter = tk.Button(Mafenetre, text ='Quitter', font=("Arial", 12, "bold"), command = Mafenetre.destroy)
Quitter.grid(row=6, column=2, sticky=tk.W, pady=4)

# widget Obligatoire
tk.Label(Mafenetre, text = '* Champs obligatoire', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=7, column=1)

Mafenetre.mainloop()



#---------BIBLIOTHEQUES/MODULES---------
import folium
import webbrowser

#----------PROGRAMME PRINCIPAL----------
# Coordonnées GPS du point central de la carte
lieu = [46.548312, 3.287667]
# Création d'une carte
carte= folium.Map(location=lieu,zoom_start=12)

# Ajout marqueur avec légende, couleur
folium.Marker(
    location=lieu,
    popup='Lycée Agricole du Bourbonnais',
    icon=folium.Icon(color='green')
    ).add_to(carte)

# Cercle de confinement en mètres (radius = 1000 pour 1 km)
folium.Circle(lieu,radius = 1000, fill=True, color='red', attr='zone 1 km' ).add_to(carte)
folium.Circle(lieu,radius = 5000, fill=True, color='orange', attr='zone 5 km'  ).add_to(carte)

# enregistrement et affichage de la carte
carte.save('carte_confinement.html')
webbrowser.open('carte_confinement.html')






#---------BIBLIOTHEQUES/MODULES---------
import folium
import webbrowser

#----------PROGRAMME PRINCIPAL----------
# Création d'une carte
carte= folium.Map(location=[46.548312, 3.287667],zoom_start=18)

# Ajout localisations et  marqueurs
accueilL = [46.548312, 3.287667]
folium.Marker(
    location=accueilL,
    popup='Accueil Lycée',
    icon=folium.Icon(color='blue')
    ).add_to(carte)

viescolaireL = [46.548090, 3.287684]
folium.Marker(
    location=viescolaireL,
    popup='Vie scolaire',
    icon=folium.Icon(color='darkred')
    ).add_to(carte)

adminL = [46.548390, 3.287769]
folium.Marker(
    location=adminL,
    popup='Administration',
    icon=folium.Icon(color='green', icon='glyphicon-folder-open')
    ).add_to(carte)

direct = [46.548478, 3.287887]
folium.Marker(
    location=direct,
    popup='Direction',
    icon=folium.Icon(color='darkgreen', icon='glyphicon-user')
    ).add_to(carte)

directA = [46.548810, 3.288412]
folium.Marker(
    location=directA,
    popup='Proviseur Adjoint',
    icon=folium.Icon(color='darkgreen', icon='glyphicon-user')
    ).add_to(carte)

secpedaL = [46.548754, 3.288479]
folium.Marker(
    location=secpedaL,
    popup='Secrétariat pédagogique',
    icon=folium.Icon(color='green')
    ).add_to(carte)

cdr = [46.548692, 3.288063]
folium.Marker(
    location=cdr,
    popup='Centre de Ressources',
    icon=folium.Icon(color='orange', icon='glyphicon-book')
    ).add_to(carte)

Infirm = [46.548086, 3.287389]
folium.Marker(
    location=Infirm,
    popup='Infirmerie',
    icon=folium.Icon(color='red', icon='glyphicon-plus-sign')
    ).add_to(carte)

amphi = [46.548069, 3.287935]
folium.Marker(
    location=amphi,
    popup='Amphithêatre',
    icon=folium.Icon(color='orange', icon='glyphicon-briefcase')
    ).add_to(carte)

salleinfoL = [46.548280, 3.287882]
folium.Marker(
    location=salleinfoL,
    popup='Salles informatiques',
    icon=folium.Icon(color='orange', icon='glyphicon-floppy-disk')
    ).add_to(carte)

burinfoL = [46.548209, 3.287514]
folium.Marker(
    location=burinfoL,
    popup='Bureau informatique',
    icon=folium.Icon(color='darkred', icon='glyphicon-floppy-disk')
    ).add_to(carte)

BatA = [46.548537, 3.288128]
folium.Marker(
    location=BatA,
    popup='Bâtiment A',
    icon=folium.Icon(color='darkpurple', icon='glyphicon-home')
    ).add_to(carte)

BatC = [46.548459, 3.289003]
folium.Marker(
    location=BatC,
    popup='Bâtiment C',
    icon=folium.Icon(color='darkpurple', icon='glyphicon-home')
    ).add_to(carte)

BatD = [46.549075, 3.288174]
folium.Marker(
    location=BatD,
    popup='Bâtiment D',
    icon=folium.Icon(color='darkpurple', icon='glyphicon-home')
    ).add_to(carte)

self = [46.547234, 3.286945]
folium.Marker(
    location=self,
    popup='Restauration',
    icon=folium.Icon(color='orange', icon='glyphicon-cutlery')
    ).add_to(carte)

Dortoir = [46.547622, 3.287714]
folium.Marker(
    location=Dortoir,
    popup='Dortoir',
    icon=folium.Icon(color='orange', icon='glyphicon-bell')
    ).add_to(carte)

# enregistrement et affichage de la carte
carte.save('carte_marqueurs.html')
webbrowser.open('carte_marqueurs.html')