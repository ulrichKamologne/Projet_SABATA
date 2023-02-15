import customtkinter
import folium
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# debut interface application
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("500x300")
        self.title("SYSTEME SABATA")
        self.minsize(600, 400)
        self.maxsize(600, 400)
        # set grid layout 1x2
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)


        self.my_frame_haut = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut.grid(row=10, column=0)
        self.my_frame_bas = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_bas.grid(row=0, column=0)
        self.button = customtkinter.CTkButton(master=self, command=self.button_callback, text="CONNECTION")
        self.button.grid(row=5, column=0)


    def button_callback(self):
        self.button.grid_forget()
        self.my_frame_haut.grid_forget()
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        print("button click")
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        self.button_1 = customtkinter.CTkButton(master=self, command=self.option_1, text="option 1")
        self.button_2 = customtkinter.CTkButton(master=self, command=self.option_2, text="option 2")
        self.button_3 = customtkinter.CTkButton(master=self, command=self.option_3, text="option 3")
        self.button_4 = customtkinter.CTkButton(master=self, command=self.option_4, text="option 4")
        self.button_param = customtkinter.CTkButton(master=self, command=self.parametre, text="parametre")

        # positionement des boutton
        self.button_1.place(x=220, y=40)
        self.button_2.place(x=220, y=80)
        self.button_3.place(x=220, y=120)
        self.button_4.place(x=220, y=160)
        self.button_param.place(x=220, y=200)

    def camera(self):
        # appersu de la camera
        video_dir = "D:\dashcam Cedric"

    def Map(self):
        # en utilisant Map
        self.c = folium.Map(location=[4.3, 1.3], zoom_start=16)

    def option_1(self):
        # camera plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        self.my_frame_bas_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_bas_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        # contenu de la page
        # Créer un objet photoimage pour utiliser l'image
        #self.photo = customtkinter.CTkImage(Image.open("D:\projet-test/touche.png"), size=(20, 20))

        self.cadre = customtkinter.CTkFrame(master=self, width=300, height=30)
        self.cadre.grid(row=10, column=0)
        # Ajouter l'image dans le bouton
        self.bouton = customtkinter.CTkButton(self.cadre, text="Click Me !", fg_color="#868282",
                                              text_color="#868282", command=self.menu)
        self.bouton.grid()
        print("un instant nous inisialison la camera")




    def option_2(self):
        # Map 2D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(1)

        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)
        self.my_frame_map = customtkinter.CTkFrame(master=self, width=400, height=339,fg_color="#C1ECE6")
        self.my_frame_map.place(x=0, y=30)
        self.my_frame_donnee = customtkinter.CTkFrame(master=self, width=190, height=339,fg_color="#ECE3E3")
        self.my_frame_donnee.place(x=410, y=30)
        self.photo1 = customtkinter.CTkImage(Image.open("D:\projet-test/tes.png"), size=(20, 20))
        self.label_map= customtkinter.CTkLabel(self, text="  Image Example",
                                                compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.label_map.pack()

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 2D")
    def option_3(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map 3D")
    def option_4(self):
        # Map 3D plus panneau de signalisation plus audio
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        print("un instant nous inisialison la camera")
        print("nous actualison le Map")
    def parametre(self):
        # reglage des parametre
        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        print("parametre modifier")
    def button_home(self):

        for w in self.winfo_children():
            w.destroy()
        self.pack_propagate(0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=10, column=0)
        self.my_frame_haut_1 = customtkinter.CTkFrame(master=self, width=600, height=30)
        self.my_frame_haut_1.grid(row=0, column=0)

        print("fin")
    # retour au menu principal
    def menu(self):
        self.destroy()

    # retour a la page precedante
    def retour(self, name):

        if name == "option_1":
            for w in self.winfo_children():
                w.destroy()
            self.pack_propagate(0)
            self.button_callback()
    # selectionn


if __name__ == "__main__":
    app = App()
    app.mainloop()

