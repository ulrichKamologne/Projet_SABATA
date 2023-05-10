'''Pour mettre limage issue de la webcam dans une frame particulière en Python, vous pouvez utiliser
la bibliothèque Tkinter pour créer une interface graphique et afficher limage dans un widget `Label`.'''

'''
Voici un exemple de code qui utilise OpenCV pour récupérer les données de la webcam et Tkinter pour 
afficher limage dans un widget `Label` :
'''
#---------BIBLIOTHEQUES/MODULES---------
# appel des Modules/Librairies nécessaires
from pyroutelib3 import Router
import folium
import webbrowser

#----------PROGRAMME PRINCIPAL----------
# coordonnées GPS départ et arrivée
eplb_park = [46.548453, 3.286341]
moulins_mairie = [46.566067 , 3.332859]
# type de déplacement : cycle, foot, horse, tram, train, car ?
router = Router("car")
# Création des points de départ et d'arrivée
depart = router.findNode(eplb_park[0],eplb_park[1])
arrivee = router.findNode(moulins_mairie[0],moulins_mairie[1])
# calcul itinéraire : test de l'existence d'une route
status, itineraire = router.doRoute(depart, arrivee)
if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, itineraire)) # liste des points du parcours
# création de la carte
carte= folium.Map(location=[(eplb_park[0]+moulins_mairie[0])/2,(eplb_park[1]+moulins_mairie[1])/2],zoom_start=15)
# ajout des points (noeuds) du parcours à la carte
for indice,coord in enumerate(routeLatLons):
    if indice%10==0:
        coord=list(coord)
        folium.Marker(coord).add_to(carte)
# ajout à la carte du tracé d'une ligne reliant les points/noeuds du parcours
itineraire_coordonnees = list(map(router.nodeLatLon, itineraire)) # liste des points du parcours
folium.PolyLine(
    itineraire_coordonnees,
    color="blue",
    weight=2.5,
    opacity=1
    ).add_to(carte)
# enregistrement et affichage de la carte
carte.save('carte.html')
webbrowser.open('carte.html')





#---------BIBLIOTHEQUES/MODULES---------
from pyroutelib3 import Router
import folium
import webbrowser
from tkinter.messagebox import * # boîte de dialogue
from tkinter import *
import tkinter as tk

#----------FONCTIONS----------
# Fonction carte
def carto():
    # Récupération des données entrées
    lieudepart = depart.get()
    longitude1 = long1.get()
    latitude1 = lat1.get()
    lieuarrivee = arrivee.get()
    longitude2 = long2.get()
    latitude2 = lat2.get()

    # lieux
    departi = [float(longitude1), float(latitude1)] #[46.548453, 3.286341]
    arriveei = [float(longitude2), float(latitude2)] #[46.566067 , 3.332859]

    #type de déplacement : cycle, foot, horse, tram, train, car ?
    router = Router("car")

    # Création des points de départ et d'arrivée
    ptdepart = router.findNode(departi[0],departi[1])
    ptarrivee = router.findNode(arriveei[0],arriveei[1])

    #print(longitude1, latitude1)

    # calcul itinéraire : test de l'existence d'une route
    status, itineraire = router.doRoute(ptdepart, ptarrivee)
    if status == 'success':
        routeLatLons = list(map(router.nodeLatLon, itineraire)) # liste des points du parcours
    # création de la carte
    carte= folium.Map(location=[(departi[0]+arriveei[0])/2,(departi[1]+arriveei[1])/2],zoom_start=14)
    # ajout des points (noeuds) du parcours à la carte
    for indice,coord in enumerate(routeLatLons):
        if indice%10==0:
            coord=list(coord)
            folium.Marker(coord).add_to(carte)
    # ajout à la carte du tracé d'une ligne reliant les points/noeuds du parcours
    itineraire_coordonnees = list(map(router.nodeLatLon, itineraire)) # liste des points du parcours
    folium.PolyLine(
        itineraire_coordonnees,
        color="blue",
        weight=2.5,
        opacity=1
        ).add_to(carte)
    # enregistrement et affichage de la carte
    nomcarte = lieudepart+'_'+lieuarrivee+'.html'
    carte.save(nomcarte)
    webbrowser.open(nomcarte)

#----------PROGRAMME PRINCIPAL----------

# Création de la fenêtre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Itinéraire')
# Taille de la fenêtre
Mafenetre.geometry("460x250")
Mafenetre.configure(bg = 'orange')
tk.Label(Mafenetre, text = 'Itinéraire',
bg = 'orange', font=("Arial", 12, "bold")).grid(row=0, column=0)

# widget Nom du Lieu de Départ
tk.Label(Mafenetre, text = 'Départ =', bg = 'orange', fg='blue', font=("Arial", 11)).grid(row=1)
depart = tk.Entry(Mafenetre, bg ='bisque', fg='blue', font=("Arial", 11))
depart.grid(row=1, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=1, column=2)
# widget Longitude
tk.Label(Mafenetre, text = 'Longitude ', bg = 'orange', fg='blue', font=("Arial", 11)).grid(row=2,column=1)
long1 = tk.Entry(Mafenetre, bg ='bisque', fg='blue', font=("Arial", 11))
long1.grid(row=3, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=3, column=2)
# widget Latitude
tk.Label(Mafenetre, text = 'Latitude ', bg = 'orange', fg='blue', font=("Arial", 11)).grid(row=2,column=3)
lat1 = tk.Entry(Mafenetre, bg ='bisque', fg='blue', font=("Arial", 11))
lat1.grid(row=3, column=3)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=3, column=4)

# widget Nom du Lieu d'Arrivée
tk.Label(Mafenetre, text = 'Arrivée =', bg = 'orange', fg='green', font=("Arial", 11)).grid(row=5)
arrivee = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
arrivee.grid(row=5, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=5, column=2)
# widget Longitude
tk.Label(Mafenetre, text = 'Longitude ', bg = 'orange', fg='green', font=("Arial", 11)).grid(row=6, column=1)
long2 = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
long2.grid(row=7, column=1)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=7, column=2)
# widget Latitude
tk.Label(Mafenetre, text = 'Latitude ', bg = 'orange', fg='green', font=("Arial", 11)).grid(row=6,column=3)
lat2 = tk.Entry(Mafenetre, bg ='bisque', fg='green', font=("Arial", 11))
lat2.grid(row=7, column=3)
tk.Label(Mafenetre, text = '*', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=7, column=4)


# widget bouton Valider
Valider = tk.Button(Mafenetre, text ='Valider', font=("Arial", 12, "bold"), command=carto)
Valider.grid(row=8, column=1, sticky=tk.W, pady=4)

# widget bouton Quitter
Quitter = tk.Button(Mafenetre, text ='Quitter', font=("Arial", 12, "bold"), command = Mafenetre.destroy)
Quitter.grid(row=8, column=3, sticky=tk.W, pady=4)

# widget Obligatoire
tk.Label(Mafenetre, text = '* Champs obligatoire', bg = 'orange', fg = 'red', font=("Arial", 11)).grid(row=9, column=1)

Mafenetre.mainloop()













#utilise exel
# ---------BIBLIOTHEQUES:MODULES---------

import xlrd         #  de traitement de ficher Microsoft Excel .xls
# https://xlrd.readthedocs.io/

import folium       # Bibliothèque/Module de gestion de cartes interactives
# https://python-visualization.github.io/folium/modules.html
# http://python.abriand.info/SNT/GeoLocalisation/GeoLocalisation.html

import webbrowser   # Bibliothèque/Module
# https://docs.python.org/fr/3/library/webbrowser.html

#----------PROGRAMME PRINCIPAL----------

# Récupérer les données dans le fichier excel .xls
leFichier = 'Donnees_Carte_ex.xls'          # chemin vers le fichier
document = xlrd.open_workbook(leFichier)    # lecture des données
feuille = document.sheet_by_index(0)        # nommer la 1ère feuille (num 0) du classeur

# Affichage informations du fichier dans la console Python
print('----------------Informations Fichier----------------')

print('Nom du fichier = ', leFichier)

nom = feuille.name      # nom de la feuille (onglet) du classeur
print('Nom de la feuille = ', nom)

n= feuille.nrows # nombre de lignes utilisées dans la feuille excel
ndonnees = n-1    # retirer 1 = enlever la ligne des descripteurs
print('Nombre de données = ', ndonnees)

# Création d'une carte à partir des données du fichier Microsoft Excel
centre = [46.548312, 3.287667]                      # coordonnées du centre de la carte affichée
carte = folium.Map(location=centre,zoom_start=11)   # donne un nom de la carte avec son centre et le facteur de zoom

for i in range(1,n):              # Boucle : Pour i=1 à n (ne pas commencer à 0 = 1ère ligne, descripteurs)
    # Pour chaque valeur de i (ligne 1, ligne 2, ..., ligne n)
    etiquette = feuille.cell_value(i,0) # etiquette = valeur donnée colonne A (num 0), ligne i
    longitude = feuille.cell_value(i,1) # longitude = valeur donnée colonne B (num 1), ligne i
    latitude = feuille.cell_value(i,2)  # latitude = valeur donnée colonne C (num 1), ligne i
    donnee = feuille.cell_value(i,3)    # donnee = valeur donnée colonne D (num 1), ligne i
    lieu = [longitude, latitude]        # lieu = coordonnées à partir des colonnes B et C, ligne i
    # Ajout marqueur aux coordonnées avec légende, couleur à la carte
    # folium.Marker(location=lieu, popup=etiquette, icon=folium.Icon(color='green')).add_to(carte)
    folium.Marker(
        location=lieu,                      # location = localisation du marqueur sur la carte
        popup=etiquette,                    # popup = nom du marqueur
        icon=folium.Icon(color='green')     # icon = forme, couleur du marqueur
        ).add_to(carte)
    # Ajout périmètre donnée(s) à la carte
    rayon = donnee*1000     # 1000 = transformer données km en m
    # folium.Circle(lieu, radius = rayon, fill=True, color='orange').add_to(carte)
    folium.Circle(
        lieu,               # localisation du marqueur sur la carte (centre du cercle)
        radius = rayon,     # radius = rayon du cercle
        fill=True,          # fill = True pour surface colorée, False pour surface non colorée
        color='orange'      # color = couleur périmètre et surface (transparence)
        ).add_to(carte)

# enregistrement et affichage de la carte
nomcarte = nom+'.html'      # nom de la carte = nom de la feuille du classeur avec extension HTML
carte.save(nomcarte)        # sauvegarder un fichier (dans le même dossier que le fichier python)
webbrowser.open(nomcarte)   # ouvrir un fichier dans un navigateur web




#Utilisation d'édupython 3 et des Modules/Librairies xlrd, folium, webbrowser, os.path2, datetime, tkinter (Rappel installation Bibliothèque/Module).

#Télécharger le fichier suivant et le placer dans le même dossier que le fichier Python.

#---------BIBLIOTHEQUES/MODULES---------
import xlrd
import os.path
import datetime
import folium
import webbrowser
from tkinter.messagebox import * # boîte de dialogue
from tkinter import *
from tkinter import filedialog
import tkinter as tk

#----------FONCTIONS----------
def ChangeF():

    LST_Types = [( 'Fichier Excel' , '.xls' )]
    leFichier = tk.filedialog.askopenfilename ( title = "Sélectionnez un fichier ..." , filetypes = LST_Types )
    if leFichier == "" : return
    if leFichier:
        document = xlrd.open_workbook(leFichier)
        feuille = document.sheet_by_index(0)
        NomF = os.path.basename(leFichier)

        # Affichage informations du fichier
        infos = StringVar()
        infos.set('Informations Fichier')
        monAffichage = Label(Mafenetre, textvariable = infos,  bg='lightgreen', font=("Arial", 12, 'bold'))
        monAffichage.grid(row=2, columnspan=2, sticky='ew' )

        leChemin = StringVar()
        NomF = os.path.basename(leFichier)
        leChemin.set('Nom du fichier = '+NomF)

        nom = str(feuille.name)
        laFeuille = StringVar()
        laFeuille.set('Nom de la feuille = '+nom)

        Modif = StringVar()
        timestamp = os.path.getmtime(leFichier)
        dateF = datetime.date.fromtimestamp(timestamp)
        Modif.set('Dernière Modification = '+str(dateF))

        nlignes = feuille.nrows
        ndonnees = str(feuille.nrows-1)
        NbreDonnees = StringVar()
        NbreDonnees.set('Nombre de données = '+ndonnees)
        monAffichage = Label(Mafenetre, textvariable = leChemin, bg='white', font=("Arial", 11))
        monAffichage.grid(row=4, columnspan=2, sticky='ew')
        monAffichage = Label(Mafenetre, textvariable = laFeuille, bg='white', font=("Arial", 11))
        monAffichage.grid(row=5, columnspan=2, sticky='ew')
        monAffichage = Label(Mafenetre, textvariable = Modif, bg='white', font=("Arial", 11))
        monAffichage.grid(row=6, columnspan=2, sticky='ew')
        monAffichage = Label(Mafenetre, textvariable = NbreDonnees, bg='white', font=("Arial", 11))
        monAffichage.grid(row=7, columnspan=2, sticky='ew')

        # Création d'une carte
        centre = [46.548312, 3.287667]
        # Lecture des données
        carte= folium.Map(location=centre,zoom_start=11)
        for i in range(1,nlignes):
            etiquette=feuille.cell_value(i,0)
            longitude=feuille.cell_value(i,1)
            latitude=feuille.cell_value(i,2)
            donnee=feuille.cell_value(i,3)
            lieu = [longitude, latitude]
        # Ajout marqueur avec légende, couleur
            folium.Marker(
                location=lieu,
                popup=etiquette,
                icon=folium.Icon(color='green')
                ).add_to(carte)
        # Périmètre donnée(s)
            perimetre = float(donnee)*1000 # 1000 = transformer données km en m
            folium.Circle(lieu,radius = perimetre, fill=True, color='orange' ).add_to(carte)
        # enregistrement et affichage de la carte
        nomcarte = nom+"_"+str(dateF)+'.html'
        carte.save(nomcarte)
        webbrowser.open(nomcarte)

#----------PROGRAMME PRINCIPAL----------
fichier=''
# Création de la fenêtre principale (main window)
Mafenetre = tk.Tk()
Mafenetre.title('Analyse')
# Taille de la fenêtre
Mafenetre.geometry('350x200')
Mafenetre.configure(bg='white')
Mafenetre.columnconfigure ( 0 , minsize = 200 , weight = 1 )
Mafenetre.columnconfigure ( 1 , minsize = 100 , weight = 1 )

debut = StringVar()
debut.set('Récupération du Fichier')
monAffichage = Label(Mafenetre, textvariable = debut,  bg='lightblue', font=("Arial", 12, 'bold'))
monAffichage.grid(row=0, columnspan=2, sticky='ew' )

# widget bouton Changer de Fichier
ChangeF = tk.Button(Mafenetre, text ='Fichier', fg='blue', font=("Arial", 12, "bold"), command= ChangeF)
ChangeF.grid(row=1, column=0, sticky='ew' )
# widget bouton Quitter
Quitter = tk.Button(Mafenetre, text ='Quitter', font=("Arial", 12, "bold"), command = Mafenetre.destroy)
Quitter.grid(row=1, column=1)

Mafenetre.mainloop()