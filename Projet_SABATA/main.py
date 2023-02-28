import customtkinter
from tkintermapview import TkinterMapView
from PIL import Image
import numpy as np
import time
#import Map_2d
import sys
from win10toast import ToastNotifier
import webbrowser
import speech_recognition as sr

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class Map3d:

    def __init__(self):
        super().__init__()


class Camera:

    def __init__(self):
        super().__init__()


class Map(customtkinter.CTk):

    def __init__ (self, parent):
        super().__init__(self, parent)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

    def search_event (self, event=None):
        self.map_widget.set_address(self.entry.get())

    def set_marker_event (self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event (self):
        for marker in self.marker_list:
            marker.delete()

    def change_appearance_mode (self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map (self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)

    def on_closing (self, event=0):
        self.destroy()

    def start (self):
        self.mainloop()


# debut interface application
class App(customtkinter.CTk):

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        # appelle
        self.photo_mode = None
        self.photo_retour = None
        self.photo_menu = None
        self.label_map = None
        self.label_p_second = None
        self.label_p_vitess = None
        self.my_frame_panneau_secondaire = None
        self.my_frame_panneau_vitesse = None
        self.my_frame_donnee = None
        self.my_frame_map = None
        self.button_param = None
        self.button_4 = None
        self.button_3 = None
        self.button_2 = None
        self.button_1 = None
        self.button_mode = None
        self.button_retour = None
        self.button_menu = None
        self.my_frame_bas = None
        self.my_frame_haut = None

        width_tk = 900
        height_tk = 500
        self.geometry("500x300")
        self.title("SYSTEME SABATA")
        self.minsize(width_tk, height_tk)
        self.maxsize(width_tk, height_tk)
        self.configure(
            fg_color="#11284A")  ##19064A, #3FC5E0, #3F0BE0, #1E1E69, #3D23F7, #19D3F7, #41B2E0,#EFD3F7 ,#EFFEF7,#19FEF7,#070D4A
        # set grid layout 1x2
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tamplet()
        # contenue de la page
        logo = customtkinter.CTkImage(Image.open("tes.png"), size=(200, 200))
        self.my_frame = customtkinter.CTkFrame(master=self, width=200, height=200)
        self.my_frame.place(x=width_tk / 2 - 100, y=50)
        self.photo = customtkinter.CTkLabel(self.my_frame, image=logo, text="")
        self.photo.place(x=0, y=0)
        self.button = customtkinter.CTkButton(master=self, command=self.connection, text="CONNECTION",
                                              width=120, height=30)
        self.button.place(x=width_tk / 2 - 60, y=height_tk / 2 + 10)

    def change_appearance_mode(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def tamplet(self):

        width_tk = 900
        # height_tk = 500
        self.my_frame_haut = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=10, column=0)
        self.my_frame_bas = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=0, column=0)
        # touche barre de tache
        # Créer un objet photo-image pour utiliser l'image
        self.photo_menu = customtkinter.CTkImage(Image.open("retour.jfif"), size=(25, 20))
        self.photo_retour = customtkinter.CTkImage(Image.open("menu.jfif"), size=(30, 25))
        self.photo_mode = customtkinter.CTkImage(Image.open("retour_2.jfif"), size=(25, 20))
        # Ajouter l'image dans le button
        self.button_menu = customtkinter.CTkButton(self.my_frame_haut, text="", image=self.photo_mode, width=25, height=25,
                                                   fg_color="#000000",
                                                   text_color="#868282", command=self.menu)
        self.button_retour = customtkinter.CTkButton(self.my_frame_haut, text="", width=25, height=25,
                                                     image=self.photo_menu, fg_color="#000000",
                                                     text_color="#868282", command=self.menu)
        self.button_mode = customtkinter.CTkButton(self.my_frame_haut, text="", width=25, height=25, image=self.photo_retour,
                                                   fg_color="#000000",
                                                   text_color="#868282", command=self.menu)
        self.button_retour.place(x=width_tk / 2 - 70, y=0)
        self.button_mode.place(x=width_tk / 2 - 20, y=0)
        self.button_menu.place(x=width_tk / 2 + 30, y=0)

    def connection(self):
        width_tk = 900
        height_tk = 500
        self.lable_recup = customtkinter.CTkLabel(self, text="recuperation des donnee ....", text_color="#868282",
                                                  compound="left",
                                                  font=customtkinter.CTkFont(size=12, weight="bold"))
        self.lable_analys = customtkinter.CTkLabel(self, text="analyse des donnee ....", text_color="#FFFFFF",
                                                   compound="left",
                                                   font=customtkinter.CTkFont(size=12, weight="bold"))
        time.sleep(0)
        self.lable_recup.place(x=width_tk / 2 - 80, y=height_tk / 2 + 50)
        print("1ier etape")
        # Connexion au Wifi
        print("nous nous connectont au reseau wifi")
        time.sleep(0)
        # my_motification= ToastNotifier()
        # my_motification.show_toast("alerte", "apareille connecte", duration=2)
        self.lable_analys.place(x=width_tk / 2 - 70, y=height_tk / 2 + 70)
        print("2ier etape")
        print("connection en cour....")
        # function execution
        time.sleep(0)
        self.button_select_option()

    def button_select_option(self):
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        width_tk = 900
        # height_tk = 500

        larger_bunt = 150
        hauteur_bnt = 30
        space_1 = 200
        space_entre_btn = 40
        # barre de tache , de menu
        self.tamplet()
        # contenue de la page
        logo = customtkinter.CTkImage(Image.open("tes.png"), size=(160, 150))
        self.my_frame = customtkinter.CTkFrame(master=self, width=160, height=150)
        self.my_frame.place(x=width_tk / 2 - 80, y=40)
        self.photo = customtkinter.CTkLabel(self.my_frame, image=logo, text="")
        self.photo.place(x=0, y=0)
        self.button_1 = customtkinter.CTkButton(master=self, command=self.option_1, text="option 1", width=larger_bunt,
                                                height=hauteur_bnt)
        self.button_2 = customtkinter.CTkButton(master=self, command=self.option_2, text="option 2", width=larger_bunt,
                                                height=hauteur_bnt)
        self.button_3 = customtkinter.CTkButton(master=self, command=self.option_3, text="option 3", width=larger_bunt,
                                                height=hauteur_bnt)
        self.button_4 = customtkinter.CTkButton(master=self, command=self.option_4, text="option 4", width=larger_bunt,
                                                height=hauteur_bnt)
        self.button_param = customtkinter.CTkButton(master=self, command=self.parametre, text="parametre",
                                                    width=larger_bunt, height=hauteur_bnt)

        # positionement des boutton
        self.button_1.place(x=width_tk / 2 - larger_bunt / 2, y=space_1)
        self.button_2.place(x=width_tk / 2 - larger_bunt / 2, y=space_1 + space_entre_btn)
        self.button_3.place(x=width_tk / 2 - larger_bunt / 2, y=space_1 + 2 * space_entre_btn)
        self.button_4.place(x=width_tk / 2 - larger_bunt / 2, y=space_1 + 3 * space_entre_btn)
        self.button_param.place(x=width_tk / 2 - larger_bunt / 2, y=space_1 + 4 * space_entre_btn)
        print("button click")

    def option_1(self):
        # camera plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        width_tk = 900
        height_tk = 500
        self.pack_propagate()

        # barre de tache , de menu
        self.tamplet()

        # contenu de la page
        self.my_frame_map = customtkinter.CTkFrame(master=self, width=width_tk - 200, height=height_tk - 60,
                                                   fg_color="#C1ECE6")
        self.my_frame_donnee = customtkinter.CTkFrame(master=self, width=200, height=height_tk - 60, fg_color="#43DBFA")
        self.my_frame_panneau_vitesse = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100, height=100,
                                                               corner_radius=75,
                                                               fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_panneau_secondaire = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100,
                                                                  height=100, corner_radius=75,
                                                                  fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_map.place(x=0, y=30)
        self.my_frame_donnee.place(x=width_tk - 198, y=30)
        self.my_frame_panneau_vitesse.place(x=50, y=40)
        self.my_frame_panneau_secondaire.place(x=50, y=180)
        # text de la fenetre
        self.label_p_vitess = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau vitesse !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_second = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau second !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_vitess.place(x=20, y=0)
        self.label_p_second.place(x=20, y=150)


        # en atente du map 2d (de la function)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement de la camera ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")

    def option_2(self):
        # Map 2D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()
        width_tk = 900
        height_tk = 500

        # barre de tache , de menu
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.Conteneur = customtkinter.CTkFrame(master=self, height=300, corner_radius=0, fg_color=None)
        self.Conteneur.grid(row=2, padx=0, sticky="nsew")
        self.my_frame_haut = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=3, column=0, sticky="nsew")

        self.Conteneur.grid_columnconfigure(0, weight=1)
        self.Conteneur.grid_columnconfigure(1, weight=0)
        self.Conteneur.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self.Conteneur, width=150, corner_radius=0, fg_color='#000000')
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self.Conteneur, corner_radius=0, fg_color="#11284A")
        self.frame_right.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_right ============
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=0)

        self.button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Set Marker",)
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Clear Markers",)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        self.map_label = customtkinter.CTkLabel(self.frame_right, text="Tile Server:", anchor="w")
        self.map_label.grid(row=2, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_right, values=["OpenStreetMap", "Google normal",
                                                                                    "Google satellite"],)
        self.map_option_menu.grid(row=2, column=0, padx=(20, 20), pady=(10, 0))


        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_left, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_left,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>")

        self.button_5 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Search",
                                                width=90)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Bandjoun")
        self.map_option_menu.set("OpenStreetMap")
        #self.appearance_mode_optionemenu.set("Dark")

        # contenu de la page
        '''self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.my_frame_map = customtkinter.CTkFrame(master=self, fg_color="#C1ECE6")
        self.my_frame_donnee = customtkinter.CTkFrame(master=self, fg_color="#43DBFA")

        self.my_frame_map.grid(row=0, column=0)
        self.my_frame_donnee.grid(row=0, column=1)
        
        # ============ frame_left ============
        self.my_frame_panneau_vitesse = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100, height=100,
                                                               corner_radius=75,
                                                               fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_panneau_secondaire = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100,
                                                                  height=100, corner_radius=75,
                                                                  fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_panneau_vitesse.place(x=50, y=40)
        self.my_frame_panneau_secondaire.place(x=50, y=180)

        self.button_1 = customtkinter.CTkButton(master=self.my_frame_donnee,
                                                text="Set Marker")
        self.button_1.place(x=50, y=300)

        self.button_2 = customtkinter.CTkButton(master=self.my_frame_donnee,
                                                text="Clear Markers")
        self.button_2.place(x=40, y=350)

        self.map_label = customtkinter.CTkLabel(self.my_frame_donnee, text="Tile Server:", anchor="w")
        self.map_label.place(x=40, y=270)
        self.map_option_menu = customtkinter.CTkOptionMenu(self.my_frame_donnee,
                                                           values=["OpenStreetMap", "Google normal",
                                                                   "Google satellite"])
        self.map_option_menu.place(x=40, y=380)

        # ============ frame_right ============

        # text de la fenetre/ contenue du map et afiche
        # text de la fenetre
        self.label_p_vitess = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau vitesse !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_second = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau second !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_vitess.place(x=20, y=0)
        self.label_p_second.place(x=20, y=150)

        # en atente du map 2d (de la function)
        self.my_frame_map.grid_rowconfigure(1, weight=1)
        self.my_frame_map.grid_rowconfigure(0, weight=0)
        self.my_frame_map.grid_columnconfigure(0, weight=1)
        self.my_frame_map.grid_columnconfigure(1, weight=0)
        self.my_frame_map.grid_columnconfigure(2, weight=1)
        self.map_widget = TkinterMapView(self.my_frame_map, corner_radius=0,width=300,height=300)
        self.map_widget.place(x=20, y=20)'''
        #self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map 2d ...",
        #                                        compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        #self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 2D")

    def option_3(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()
        width_tk = 900
        height_tk = 500

        # barre de tache , de menu
        self.tamplet()
        # contenu de la page
        self.my_frame_map = customtkinter.CTkFrame(master=self, width=width_tk - 200, height=height_tk - 60,
                                                   fg_color="#C1ECE6")
        self.my_frame_donnee = customtkinter.CTkFrame(master=self, width=200, height=height_tk - 60, fg_color="#43DBFA")
        self.my_frame_panneau_vitesse = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100, height=100,
                                                               corner_radius=75,
                                                               fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_panneau_secondaire = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100,
                                                                  height=100, corner_radius=75,
                                                                  fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_map.place(x=0, y=30)
        self.my_frame_donnee.place(x=width_tk - 198, y=30)
        self.my_frame_panneau_vitesse.place(x=50, y=40)
        self.my_frame_panneau_secondaire.place(x=50, y=180)
        # text de la fenetre
        self.label_p_vitess = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau vitesse !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_second = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau second !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_vitess.place(x=20, y=0)
        self.label_p_second.place(x=20, y=150)

        # en atente du map 2d (de la function)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map 3d ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 3D")

    def option_4(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()
        width_tk = 900
        height_tk = 500

        # barre de tache , de menu
        self.tamplet()
        # contenu de la page
        self.my_frame_map = customtkinter.CTkFrame(master=self, width=width_tk - 200, height=height_tk - 60,
                                                   fg_color="#C1ECE6")
        self.my_frame_donnee = customtkinter.CTkFrame(master=self, width=200, height=height_tk - 60, fg_color="#43DBFA")
        self.my_frame_panneau_vitesse = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100, height=100,
                                                               corner_radius=75,
                                                               fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_panneau_secondaire = customtkinter.CTkFrame(master=self.my_frame_donnee, width=100,
                                                                  height=100, corner_radius=75,
                                                                  fg_color="#FFFFFF", border_color="#FFFFFF")
        self.my_frame_map.place(x=0, y=30)
        self.my_frame_donnee.place(x=width_tk - 198, y=30)
        self.my_frame_panneau_vitesse.place(x=50, y=40)
        self.my_frame_panneau_secondaire.place(x=50, y=180)
        # text de la fenetre
        self.label_p_vitess = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau vitesse !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_second = customtkinter.CTkLabel(self.my_frame_donnee, text="panneau second !",
                                                     compound="left",
                                                     font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_p_vitess.place(x=20, y=0)
        self.label_p_second.place(x=20, y=150)

        # en atente du map 2d (de la function)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map")

    def parametre(self):
        # reglage des parametre
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()
        # width_tk = 900
        # height_tk = 50

        # barre de tache , de menu
        self.tamplet()

        print("parameter modifier")

    # function des touche
    def mode(self):

        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()

    # retour au menu principal
    def menu(self):
        self.destroy()

    # retour a la page precedente
    def retour(self, name):
        pass

    # selection

if __name__ == "__main__":
    start = time.time()
    app = App()
    app.mainloop()
    end = time.time()
    print(end - start)


