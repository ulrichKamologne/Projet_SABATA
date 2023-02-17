import customtkinter
import folium
from PIL import Image
import numpy as np

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class Map3d:

    def __init__(self):
        super().__init__()


class Camera:

    def __init__(self):
        super().__init__()


class Map2d:

    def __init__(self):
        super().__init__()
        longitude = 1.33
        latitude = 42
        tail_zoom = 20
        c = folium.Map(location=[longitude, latitude], zoom_start=tail_zoom)
        c.save("map.html")


# debut interface application
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.button_param = None
        self.button_4 = None
        self.button_3 = None
        self.button_2 = None
        self.button_1 = None
        self.button_menu = None
        self.my_frame_bas_1 = None
        self.my_frame_haut_1 = None
        width_tk = 900
        height_tk = 500
        self.geometry("500x300")
        self.title("SYSTEME SABATA")
        self.minsize(width_tk, height_tk)
        self.maxsize(width_tk, height_tk)
        self.configure(fg_color="#11284A") ##19064A, #3FC5E0, #3F0BE0, #1E1E69, #3D23F7, #19D3F7, #41B2E0,#EFD3F7 ,#EFFEF7,#19FEF7,#070D4A
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
        self.button = customtkinter.CTkButton(master=self, command=self.button_select_option, text="CONNECTION",
                                              width=120, height=30)
        self.button.place(x=width_tk / 2 - 60, y=height_tk / 2 + 10)

    def tamplet(self):

        width_tk = 900
        height_tk = 500
        self.my_frame_haut = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#3C3F3F",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=10, column=0)
        self.my_frame_bas = customtkinter.CTkFrame(master=self, width=width_tk, height=30, fg_color="#3C3F3F",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=0, column=0)
        # touche barre de tache
        # Créer un objet photo-image pour utiliser l'image
        self.photo = customtkinter.CTkImage(Image.open("retour.png"), size=(25, 20))
        # Ajouter l'image dans le button
        self.button_menu = customtkinter.CTkButton(self.my_frame_haut, text="", image=self.photo, width=25, height=25,
                                                   fg_color="#3C3F3F",
                                                   text_color="#868282", command=self.menu)
        self.button_retour = customtkinter.CTkButton(self.my_frame_haut, text="", width=25, height=25,
                                                     image=self.photo, fg_color="#3C3F3F",
                                                     text_color="#868282", command=self.menu)
        self.button_mode = customtkinter.CTkButton(self.my_frame_haut, text="", width=25, height=25, image=self.photo,
                                                   fg_color="#3C3F3F",
                                                   text_color="#868282", command=self.menu)
        self.button_retour.place(x=width_tk / 2 - 70, y=0)
        self.button_menu.place(x=width_tk / 2 - 20, y=0)
        self.button_mode.place(x=width_tk / 2 + 30, y=0)

    def button_select_option(self):
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        width_tk = 900
        height_tk = 500
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
        self.pack_propagate(0)

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

        # en atente du map 2d (de la fonction)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement de la camera ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")

    def option_2(self):
        # Map 2D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(1)
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

        # en atente du map 2d (de la fonction)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map 2d ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 2D")

    def option_3(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
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

        # en atente du map 2d (de la fonction)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map 3d ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 3D")

    def option_4(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
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

        # en atente du map 2d (de la fonction)
        self.label_map = customtkinter.CTkLabel(self.my_frame_map, text=" chargement du Map ...",
                                                compound="left", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label_map.place(x=(width_tk - 400) / 2, y=(height_tk - 60) / 2)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map")

    def parametre(self):
        # reglage des parametre
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        width_tk = 900
        height_tk = 50

        # barre de tache , de menu
        self.tamplet()

        print("parameter modifier")

    # function des touche

    def mode(self):

        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)

    # retour au menu principal
    def menu(self):
        self.destroy()

    # retour a la page precedente
    def retour(self, name):

        if name == "option_1":
            for w in self.winfo_children():
                w.destroy()
            self.pack_propagate(0)
            self.button_callback()
    # selection


if __name__ == "__main__":
    app = App()
    app.mainloop()
