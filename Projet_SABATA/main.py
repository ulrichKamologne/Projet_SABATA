import customtkinter
from tkintermapview import TkinterMapView
from PIL import Image
import numpy as np
import time
import network
# import Map_2d
import sys
from win10toast import ToastNotifier
import webbrowser
import speech_recognition as sr

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# debut interface application
class App(customtkinter.CTk):
    scale = 1
    color_of_Fame = "#11284A"
    width_tk = 900
    height_tk = 500
    larger_bunt = 200
    hauteur_bnt = 30

    def __init__ (self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        # appelle

        self.geometry("500x300")
        self.title("SYSTEME SABATA")
        self.minsize(App.width_tk, App.height_tk)
        self.maxsize(App.width_tk, App.height_tk)
        self.configure(fg_color="#11284A")  ##19064A, #3FC5E0, #3F0BE0, #1E1E69, #3D23F7
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        if App.scale >= 1:
            nsew = 'nsew'
        else:
            nsew = ''
        # contenue de la page
        logo = customtkinter.CTkImage(Image.open("tes.png"), size=(200, 200))  # size=(App.width_tk, App.height_tk)
        my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        my_frame.grid(row=0, column=0, sticky=nsew)

        my_frame.grid_rowconfigure(0, weight=1)
        my_frame.grid_columnconfigure(0, weight=1)

        self.photo = customtkinter.CTkLabel(my_frame, image=logo, text="")
        self.photo.grid(row=0, column=0)

        self.frames = {}

        for F in (page_connect, page_option, option_1, option_2, option_3, option_4, parametre, page_connect):
            frame = F(my_frame)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.after(2500, self.show_frame, page_connect)

    def show_frame (self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def retour(self):
        pass

    def bar_de_tache (self, name):
        # show selected frame
        if name == "option_1" or "option_2" or "option_3" or "option_4":
            page_option

        if name == "page_option":
            page_connect

        if name == "page_connect":
            pass

    def change_appearance_mode (self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)


# premiere page contenant le bouton connection
class page_connect(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=0)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_rowconfigure(2, weight=0)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=0)
        self.my_frame.grid_columnconfigure(2, weight=1)
        logo = customtkinter.CTkImage(Image.open("tes.png"), size=(200, 200))
        self.photo = customtkinter.CTkLabel(self.my_frame, image=logo, text="")
        self.photo.grid(row=0, column=1, sticky="nesw", pady=(20, 20))
        self.button = customtkinter.CTkButton(master=self.my_frame, text="CONNECTION",
                                              width=120, height=30, command=lambda: app.show_frame(page_option))
        self.button.grid(row=1, column=1, sticky="n")

# deuxieme page contenant les option
class page_option(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=0)
        self.my_frame.grid_rowconfigure(1, weight=0)
        self.my_frame.grid_rowconfigure(3, weight=0)
        self.my_frame.grid_rowconfigure(4, weight=0)
        self.my_frame.grid_rowconfigure(5, weight=0)
        self.my_frame.grid_rowconfigure(6, weight=0)
        self.my_frame.grid_rowconfigure(7, weight=0)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.my_frame.grid_columnconfigure(1, weight=0)
        self.my_frame.grid_columnconfigure(2, weight=1)
        logo = customtkinter.CTkImage(Image.open("tes.png"), size=(200, 150))
        self.photo = customtkinter.CTkLabel(self.my_frame, image=logo, text="")
        self.photo.grid(row=0, column=1, pady=(20, 10))
        self.button_1 = customtkinter.CTkButton(master=self.my_frame, command=lambda: app.show_frame(option_1),
                                                text="option 1", width=App.larger_bunt,
                                                height=App.hauteur_bnt)
        self.button_2 = customtkinter.CTkButton(master=self.my_frame, command=lambda: app.show_frame(option_2),
                                                text="option 2", width=App.larger_bunt,
                                                height=App.hauteur_bnt)
        self.button_3 = customtkinter.CTkButton(master=self.my_frame, command=lambda: app.show_frame(option_3),
                                                text="option 3", width=App.larger_bunt,
                                                height=App.hauteur_bnt)
        self.button_4 = customtkinter.CTkButton(master=self.my_frame, command=lambda: app.show_frame(option_4),
                                                text="option 4", width=App.larger_bunt,
                                                height=App.hauteur_bnt)
        self.button_param = customtkinter.CTkButton(master=self.my_frame, command= lambda: app.show_frame(parametre),
                                                    text="parametre",
                                                    width=App.larger_bunt, height=App.hauteur_bnt)

        # positionement des boutton
        self.button_1.grid(row=1, column=1, pady=(10, 10))
        self.button_2.grid(row=2, column=1, pady=(10, 10))
        self.button_3.grid(row=3, column=1, pady=(10, 10))
        self.button_4.grid(row=4, column=1, pady=(10, 10))
        self.button_param.grid(row=5, column=1, pady=(10, 10))

        # verification
        print("button click")

    def two_funcs(self, *funcs):
        def two_funcs(*args, **kwargs):
            for f in funcs:
                f(*args, **kwargs)
        return two_funcs
    def wifi(self):
        pass
        '''
        # Connexion au Wifi

        WIFI_SSID = 'TECNO CAMON 12 Air'
        WIFI_PASSWORD = 'kengnetherese'

        # Desactive le reseau Wifi interne a la carte
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active (False)

        # connection de la carte au reseau Wifi
        wlan = network.WLAN(network.STA_IF)
        wlan.active (True)
        time.sleep (3)
        print ('connexion au reseau...')
        wlan.connect (WIFI_SSID, WIFI_PASSWORD)
        time.sleep (1)
        # 20 Tentatives de connexions au Wifi
        MAX_ATTEMPTS = 20
        attempt_count = 0

        while not wlan.isconnected () and attempt_count < MAX_ATTEMPTS:
            attempt_count += 1
            time.sleep(1)
            wlan.connect(WIFI_SSID, WIFI_PASSWORD)

        if attempt_count == MAX_ATTEMPTS:
            print('impossible de rejoindre le reseau Wifi')
            sys.exit()
        print('config reseau:', wlan.ifconfig())
        '''
# page contenant l'option_1
class option_1(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.frame_camera = customtkinter.CTkFrame(master=self.my_frame, fg_color="#000000",
                                                   corner_radius=0, height=App.height_tk)
        self.frame_camera.grid(row=0, column=0, sticky="nesw", pady=(1, 1))
        self.frame_donnee = customtkinter.CTkFrame(master=self.my_frame, fg_color="#FFFFFF",
                                                   corner_radius=0)
        self.frame_donnee.grid(row=0, column=1, sticky="nesw", pady=(1, 1))

        # verification
        print("initialisation de la camera")


class option_2(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.frame_camera = customtkinter.CTkFrame(master=self.my_frame, fg_color="#000000",
                                                   corner_radius=0, height=App.height_tk)
        self.frame_camera.grid(row=0, column=0, sticky="nesw", pady=(1, 1))
        self.frame_donnee = customtkinter.CTkFrame(master=self.my_frame, fg_color="#FFFFFF",
                                                   corner_radius=0)
        self.frame_donnee.grid(row=0, column=1, sticky="nesw", pady=(1, 1))

        # Map 2D plus panneau de signalisation plus audio

        # ============ frame_right(frame_donnee) ============
        self.frame_donnee.grid_columnconfigure(0, weight=0)
        self.frame_donnee.grid_rowconfigure(0, weight=1)
        self.frame_donnee.grid_rowconfigure(1, weight=1)
        self.frame_donnee.grid_rowconfigure(2, weight=0)
        self.frame_donnee.grid_rowconfigure(3, weight=0)
        self.frame_donnee.grid_rowconfigure(4, weight=0)

        self.button_1 = customtkinter.CTkButton(master=self.frame_donnee,
                                                text="Set Marker", command= self.start)
        self.button_1.grid(pady=(10, 0), padx=(20, 20), row=2, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_donnee,
                                                text="Clear Markers", command= self.on_closing)
        self.button_2.grid(pady=(10, 0), padx=(20, 20), row=3, column=0)

        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_donnee, values=["OpenStreetMap", "Google normal",
                                                                                     "Google satellite"], command= self.change_map)
        self.map_option_menu.grid(row=4, column=0, padx=(20, 20), pady=(10, 10))

        # ============ frame_left(frame_camera) ============

        self.frame_camera.grid_columnconfigure(0, weight=1)
        self.frame_camera.grid_rowconfigure(0, weight=0)
        self.frame_camera.grid_rowconfigure(1, weight=1)
        self.marker_list = []
        self.map_widget = TkinterMapView(self.frame_camera, corner_radius=0, height= App.height_tk)
        self.map_widget.grid(row=1, column=0,  sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_camera,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 110), pady=12)
        self.entry.bind("<Return>")

        self.button_5 = customtkinter.CTkButton(master=self.frame_camera,
                                                text="Search",
                                                width=90, command= self.search_event)
        self.button_5.grid(row=0, column=0, sticky="e", padx=(12, 10), pady=12)
        # Set default values
        self.map_widget.set_address("Bandjoun", marker=True)
        self.map_option_menu.set("OpenStreetMap")
        self.map_widget.set_zoom(25)
        self.map_widget.add_left_click_map_command (self.left_click_event)
    def left_click_event (self, coordinates_tuple):
        print ("Left click event with coordinates:", coordinates_tuple)
        self.map_widget.set_zoom(25)


        #self.map_widget.set_position(36.1699, -115.1396)
        #self.map_widget.set_zoom(15)
        # self.appearance_mode_optionemenu.set("Dark")

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 2D")

        # verification
        print("initialisation de la camera")

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
            self.map_widget.set_tile_server ("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server ("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                             max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server ("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                             max_zoom=22)

    def on_closing (self, event=0):
        self.destroy()

    def start (self):
        self.mainloop()


class option_3(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.frame_camera = customtkinter.CTkFrame(master=self.my_frame, fg_color="#000000",
                                                   corner_radius=0, height=App.height_tk)
        self.frame_camera.grid(row=0, column=0, sticky="nesw", pady=(1, 1))
        self.frame_donnee = customtkinter.CTkFrame(master=self.my_frame, fg_color="#FFFFFF",
                                                   corner_radius=0)
        self.frame_donnee.grid(row=0, column=1, sticky="nesw", pady=(1, 1))

        # verification
        print("initialisation de la camera")
        print("nous actualison le Map 3D")


class option_4(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.frame_camera = customtkinter.CTkFrame(master=self.my_frame, fg_color="#000000",
                                                   corner_radius=0, height=App.height_tk)
        self.frame_camera.grid(row=0, column=0, sticky="nesw", pady=(1, 1))
        self.frame_donnee = customtkinter.CTkFrame(master=self.my_frame, fg_color="#FFFFFF",
                                                   corner_radius=0)
        self.frame_donnee.grid(row=0, column=1, sticky="nesw", pady=(1, 1))

        # verification
        print("initialisation de la camera")
        print ("nous actualison le Map")


class parametre(customtkinter.CTkFrame):
    def __init__ (self, parent):
        customtkinter.CTkFrame.__init__(self, parent)
        self.configure(fg_color=App.color_of_Fame, corner_radius=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)
        self.my_frame_haut = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                    corner_radius=0)
        self.my_frame_haut.grid(row=0, column=0, sticky="nsew")
        self.my_frame = customtkinter.CTkFrame(master=self, corner_radius=0, fg_color=App.color_of_Fame)
        self.my_frame.grid(row=1, column=0, sticky="nesw")
        self.my_frame_bas = customtkinter.CTkFrame(master=self, height=30, fg_color="#000000",
                                                   corner_radius=0)
        self.my_frame_bas.grid(row=2, column=0, sticky="nesw")

        self.my_frame.grid_rowconfigure(0, weight=1)
        self.my_frame.grid_rowconfigure(1, weight=1)
        self.my_frame.grid_columnconfigure(0, weight=1)
        self.frame_camera = customtkinter.CTkFrame(master=self.my_frame, fg_color="#000000",
                                                   corner_radius=0, height=App.height_tk)
        self.frame_camera.grid(row=0, column=0, sticky="nesw", pady=(1, 1))
        self.frame_donnee = customtkinter.CTkFrame(master=self.my_frame, fg_color="#FFFFFF",
                                                   corner_radius=0)
        self.frame_donnee.grid(row=0, column=1, sticky="nesw", pady=(1, 1))

        # verification
        print("parameter modifier")


class after:
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    # function des touche
    def mode (self):

        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate()

    # retour au menu principal
    def menu (self):
        self.destroy()

    # retour a la page precedente
    def retour (self, name):
        pass

    # selection


if __name__ == "__main__":
    start = time.time()
    app = App()
    app.mainloop()
    end = time.time()
    print(end - start)
