import customtkinter
import PIL.Image
import qrcode


class Icon:
    nombre_cree = 0

    def __init__(self, parent, nom, police, source_image, taille, xligne, ycolone):
        Icon.nombre_cree += 1
        self.parent = parent
        self.nom = nom
        self.police = int(police)
        self.source_image = source_image
        self.taille = int(taille)
        self.xligne = xligne
        self.ycolone = ycolone

    def creer(self):
        frame = customtkinter.CTkFrame(self.parent, width=self.taille, height=self.taille, fg_color="#0F0332")
        frame.grid(row=self.xligne, column=self.ycolone, padx=5)
        frame.grid_rowconfigure(0)
        frame.grid_rowconfigure(1)
        program = """img = customtkinter.CTkImage(light_image=PIL.Image.open(self.source_image), size=(self.taille, self.taille))\nimage = customtkinter.CTkButton(frame, width=self.taille, fg_color="#0F0332", height=self.taille, image=img, text="",
        command= lambda: app.show_frame(PageIcon""" + str(Icon.nombre_cree) + ")) \nimage.grid(row=0, column=0)"
        exec(program)
        label = customtkinter.CTkLabel(frame, text=self.nom, fg_color="#0F0332",
                                       font=customtkinter.CTkFont(family="Inter", size=self.police),
                                       text_color="#FFFFFF")
        label.grid(row=1, column=0)


class App(customtkinter.CTk):
    scale = 1
    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"
    default_text_size = 12 * scale
    home_icon_dimen = 50 * scale
    default_icon_dimen = 70 * scale

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)

        self.geometry("835.8x583.8")
        self.title("LIION ASSIST")
        self.minsize(int(836), int(584))
        self.maxsize(int(836), int(584))
        self.configure(fg_color="#001200")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # creating a container
        if App.scale >= 1:
            nsew = 'nsew'
        else:
            nsew = ''
        container = customtkinter.CTkFrame(self, corner_radius=0)  # , width=int(1836*App.scale), height=int(584*App.scale))
        container.grid(row=0, column=0, sticky=nsew)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
                StartPage, ConnectionPage, HomePage, PageIcon1, PageIcon2, PageIcon3, PageIcon4, PageIcon5, PageIcon6):
            frame = F(container)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # self.show_frame(StartPage)
        self.after(0, self.show_frame, StartPage)
        self.after(2500, self.show_frame, ConnectionPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        # app configuration
        self.configure(fg_color=App.default_bg_color, corner_radius=0)

        # create 2x2 grid system
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        #
        frame = customtkinter.CTkFrame(self, fg_color=App.default_bg_color)
        frame.grid(row=1, column=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"),
                                      size=(int(128 * App.scale), int(164 * App.scale)))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=int(14 * App.scale),
                                        font=customtkinter.CTkFont(family="Inter", size=int(20 * App.scale)),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=int(10 * App.scale),
                                        font=customtkinter.CTkFont(family="Inter", size=int(10 * App.scale)),
                                        text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)


class ConnectionPage(customtkinter.CTkFrame):

    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        text_instruction = """Pour connecter votre téléphone à votre console multimedia, suivez les étapes suivantes ci dessous: 
                        1.  Ouvrez l'application LIION ASSIST sur votre smartphone; Bien vouloir la télécharger 
                             sur le Playstore si elle n'est pas encore installée ;
                        2.  Autorisez l'accès à l'appareil photo, au WIFI, et au micro puis, cliquer sur le bouton
                             CONNECTER pour établir la connection ;
                        3.  Positionnez votre téléphone face à la console pour scanner le code QR ci dessus ;
                        4.  Une fois connecté, vous pouvez à présent jouir des fonctionnalités offertes par 
                             LIION ASSIST."""

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=150 * App.scale,
            border=1
        )
        code = "ce_texte_est_un_code"
        qr.add_data(code)
        qr.make(fit=True)
        img_qr = qr.make_image(fill_color="black", back_color="white")
        img_qr.save("images/qrcode.png")

        #
        frame = customtkinter.CTkFrame(self, fg_color=App.default_bg_color)
        frame.grid(row=0, column=1, pady=20)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=0)
        frame.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"),
                                      size=(int(64 * App.scale), int(82 * App.scale)))
        photo = customtkinter.CTkLabel(frame, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e", ipadx=int(17 / App.scale))
        label1 = customtkinter.CTkLabel(frame, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=12),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        img_qrcode = customtkinter.CTkImage(light_image=PIL.Image.open("images/qrcode.png"),
                                            size=(int(150 * App.scale), int(150 * App.scale)))
        qrframe = customtkinter.CTkLabel(self, width=int(150 * App.scale), height=int(150 * App.scale),
                                         image=img_qrcode, text="")
        qrframe.grid(row=1, column=1)
        label3 = customtkinter.CTkLabel(self, text=text_instruction, width=150,
                                        font=customtkinter.CTkFont(family="Inter", size=int(App.default_text_size)),
                                        text_color=App.default_text_color, justify=customtkinter.LEFT)
        label3.grid(row=3, column=1, pady=30)

        #
        bouton_suivant1 = customtkinter.CTkButton(self, text="Suivant", width=50, height=20,
                                                  command=lambda: app.show_frame(HomePage))
        bouton_suivant1.grid(row=4, column=1)


class HomePage(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_logo = customtkinter.CTkFrame(self, fg_color=App.default_bg_color, width=100)
        frame_logo.grid(row=1, column=2)
        frame_logo.grid_rowconfigure(0, weight=1)
        frame_logo.grid_rowconfigure(1, weight=0)
        frame_logo.grid_rowconfigure(2, weight=0)
        logo = customtkinter.CTkImage(light_image=PIL.Image.open("images/logo.png"), size=(92, 117))
        photo = customtkinter.CTkLabel(frame_logo, image=logo, text="")
        photo.grid(row=0, column=0, sticky="e")
        label1 = customtkinter.CTkLabel(frame_logo, text="LIION ASSIST", height=14,
                                        font=customtkinter.CTkFont(family="Inter", size=15),
                                        text_color="#FFFFFF", anchor="n")
        label1.grid(row=1, column=0)
        label2 = customtkinter.CTkLabel(frame_logo, text="STAY FOCUSED ON THE ROAD", height=10,
                                        font=customtkinter.CTkFont(family="Inter", size=7), text_color="#EAA623",
                                        anchor="n")
        label2.grid(row=2, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        # cadre des icones
        barnav_frame = customtkinter.CTkFrame(self, fg_color=App.default_bg_color)
        barnav_frame.grid(row=2, column=1, rowspan=1, columnspan=3)

        #
        Icon.nombre_cree = 0
        phone_icon = Icon(barnav_frame, "Telephone", App.default_text_size, "images/phone.png",
                          App.default_icon_dimen, 0, 0)
        phone_icon.creer()
        gps_icon = Icon(barnav_frame, "GPS", App.default_text_size, "images/gps.png",
                        App.default_icon_dimen, 0, 1)
        gps_icon.creer()
        musique_icon = Icon(barnav_frame, "Music", App.default_text_size, "images/music.png",
                            App.default_icon_dimen, 0, 2)
        musique_icon.creer()
        video_icon = Icon(barnav_frame, "Videos", App.default_text_size, "images/video.png",
                          App.default_icon_dimen, 0, 3)
        video_icon.creer()
        settings_icon = Icon(barnav_frame, "Parametres", App.default_text_size, "images/settings.png",
                             App.default_icon_dimen, 0, 4)
        settings_icon.creer()
        sms_icon = Icon(barnav_frame, "Messages", App.default_text_size, "images/sms.png",
                        App.default_icon_dimen, 0, 5)
        sms_icon.creer()


class PageIcon1(customtkinter.CTkFrame):  # phone page class
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_phone = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                             fg_color=App.default_bar_color)
        frame_phone.grid(row=1, column=0, pady=20, sticky='esw')
        frame_phone.grid_rowconfigure(0, weight=1)
        img_phone = customtkinter.CTkImage(light_image=PIL.Image.open("images/phone.png"),
                                           size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_phone = customtkinter.CTkButton(frame_phone, width=int(App.home_icon_dimen),
                                              height=int(App.home_icon_dimen), image=img_phone, text="",
                                              command=lambda: app.show_frame(HomePage), fg_color=App.default_bar_color)
        image_phone.grid(row=0, column=0)


class PageIcon2(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_gps = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                           fg_color=App.default_bar_color)
        frame_gps.grid(row=1, column=0, pady=20, sticky='esw')
        frame_gps.grid_rowconfigure(0, weight=1)
        img_gps = customtkinter.CTkImage(light_image=PIL.Image.open("images/gps.png"),
                                         size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_gps = customtkinter.CTkButton(frame_gps, width=int(App.home_icon_dimen),
                                            height=int(App.home_icon_dimen), image=img_gps, text="",
                                            command=lambda: app.show_frame(HomePage), fg_color=App.default_bar_color)
        image_gps.grid(row=0, column=0)


class PageIcon3(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_music = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                             fg_color=App.default_bar_color)
        frame_music.grid(row=1, column=0, pady=20, sticky='esw')
        frame_music.grid_rowconfigure(0, weight=1)
        img_music = customtkinter.CTkImage(light_image=PIL.Image.open("images/music.png"),
                                           size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_music = customtkinter.CTkButton(frame_music, width=int(App.home_icon_dimen),
                                              height=int(App.home_icon_dimen), image=img_music, text="",
                                              command=lambda: app.show_frame(HomePage), fg_color=App.default_bar_color)
        image_music.grid(row=0, column=0)


class PageIcon4(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_video = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                             fg_color=App.default_bar_color)
        frame_video.grid(row=1, column=0, pady=20, sticky='esw')
        frame_video.grid_rowconfigure(0, weight=1)
        img_video = customtkinter.CTkImage(light_image=PIL.Image.open("images/video.png"),
                                           size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_video = customtkinter.CTkButton(frame_video, width=int(App.home_icon_dimen),
                                              height=int(App.home_icon_dimen), image=img_video, text="",
                                              command=lambda: app.show_frame(HomePage), fg_color=App.default_bar_color)
        image_video.grid(row=0, column=0)


class PageIcon5(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_settings = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                                fg_color=App.default_bar_color)
        frame_settings.grid(row=1, column=0, pady=20, sticky='esw')
        frame_settings.grid_rowconfigure(0, weight=1)
        img_settings = customtkinter.CTkImage(light_image=PIL.Image.open("images/settings.png"),
                                              size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_settings = customtkinter.CTkButton(frame_settings, width=int(App.home_icon_dimen),
                                                 height=int(App.home_icon_dimen), image=img_settings, text="",
                                                 command=lambda: app.show_frame(HomePage),
                                                 fg_color=App.default_bar_color)
        image_settings.grid(row=0, column=0)


class PageIcon6(customtkinter.CTkFrame):
    def __init__(self, parent):
        customtkinter.CTkFrame.__init__(self, parent)

        self.configure(fg_color=App.default_bg_color, corner_radius=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        # self.grid_columnconfigure(3, weight=1)

        # cadre barre verticale de taches
        barinf_cadre = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#39585B")
        barinf_cadre.grid(row=0, column=0, rowspan=3, columnspan=1, sticky="nesw")
        barinf_cadre.grid_rowconfigure(0, weight=0)
        barinf_cadre.grid_rowconfigure(1, weight=1)
        barinf_cadre.grid_rowconfigure(2, weight=0)

        #
        home_frame = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                            fg_color=App.default_bar_color)
        home_frame.grid(row=2, column=0, pady=20, sticky='nesw')
        home_frame.grid_rowconfigure(0, weight=1)
        img_home = customtkinter.CTkImage(light_image=PIL.Image.open("images/home.png"), size=(int(App.home_icon_dimen),
                                                                                               int(App.home_icon_dimen)))
        image_home = customtkinter.CTkButton(home_frame, width=int(App.home_icon_dimen),
                                             height=int(App.home_icon_dimen),
                                             image=img_home, text="", command=self.quit,
                                             fg_color=App.default_bar_color)
        image_home.grid(row=0, column=0)

        #
        frame_time = customtkinter.CTkFrame(barinf_cadre, fg_color=App.default_bar_color,
                                            width=int(App.home_icon_dimen),
                                            height=30)
        frame_time.grid(row=0, column=0)
        frame_time.grid_rowconfigure(0, weight=1)
        frame_time.grid_rowconfigure(1, weight=1)
        heure = customtkinter.CTkLabel(frame_time, text="15:45", fg_color=App.default_bar_color,
                                       font=customtkinter.CTkFont(family="Inter",
                                                                  size=int(App.default_text_size + 8 * App.scale)),
                                       text_color="#FFFFFF")
        heure.grid(row=0, column=0)
        date = customtkinter.CTkLabel(frame_time, text="18/02/2023", fg_color=App.default_bar_color,
                                      font=customtkinter.CTkFont(family="Inter",
                                                                 size=int(App.default_text_size - 2 * App.scale)),
                                      text_color="#FFFFFF")
        date.grid(row=1, column=0)

        #
        frame_sms = customtkinter.CTkFrame(barinf_cadre, width=int(App.home_icon_dimen),
                                           fg_color=App.default_bar_color)
        frame_sms.grid(row=1, column=0, pady=20, sticky='esw')
        frame_sms.grid_rowconfigure(0, weight=1)
        img_sms = customtkinter.CTkImage(light_image=PIL.Image.open("images/sms.png"),
                                         size=(int(App.home_icon_dimen), int(App.home_icon_dimen)))
        image_sms = customtkinter.CTkButton(frame_sms, width=int(App.home_icon_dimen),
                                            height=int(App.home_icon_dimen), image=img_sms, text="",
                                            command=lambda: app.show_frame(HomePage), fg_color=App.default_bar_color)
        image_sms.grid(row=0, column=0)

        #
        title_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#D9D9D9", height=30)
        title_frame.grid(row=0, column=1, rowspan=1, columnspan=2, sticky="nesw")

        #
        right_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#FFFFFF")
        right_frame.grid(row=1, column=1, rowspan=3, columnspan=1, sticky="nesw")
        right_frame.grid_columnconfigure(0, weight=1)

        search_bar = customtkinter.CTkEntry(right_frame, height=30, corner_radius=15, fg_color="#D9D9D9",
                                            text_color="#4E4C4C", placeholder_text="Rechercher des conversations",
                                            border_color="#D9D9D9")
        search_bar.grid(row=0, column=0, padx=10, pady=15, sticky="ew")
        dicussion1 = Discussion(right_frame, "papa", 9)
        dicussion1.creer_right(1)
        dicussion2 = Discussion(right_frame, "papa", 9)
        dicussion2.creer_right(2)
        dicussion3 = Discussion(right_frame, "papa", 9)
        dicussion3.creer_right(3)

        #
        left_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#BCDAFF")
        left_frame.grid(row=1, column=2, rowspan=3, columnspan=1, sticky="nesw")


class Discussion(customtkinter.CTkFrame):
    color = "#1E7910"

    def __init__(self, parent, nom, numero):
        self.nom = nom
        self.numero = numero
        self.parent = parent
        self.height = 50

    def creer_right(self, ligne):
        theme_color = "#D9D9D9"
        label_color = "#000000"
        msg_color = "#4E4C4C"
        container = customtkinter.CTkButton(self.parent, height=self.height, fg_color=theme_color, corner_radius=12,
                                            text="", hover_color=theme_color)
        container.grid(row=ligne, column=0, padx=10, pady=5, sticky="ew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=0)
        container.grid_columnconfigure(0, weight=0)
        container.grid_columnconfigure(1, weight=1)

        cercle = customtkinter.CTkFrame(container, fg_color=Discussion.color, height=50, width=50, corner_radius=25)
        cercle.grid(row=0, column=0, rowspan=2, padx=5)
        frame_cercle = customtkinter.CTkLabel(container, fg_color=Discussion.color, height=18, width=18,
                                              text=self.nom[0].upper(),
                                              font=customtkinter.CTkFont(family="Inter", size=30, weight="bold"))
        frame_cercle.grid(row=0, column=0, rowspan=2, padx=5)

        frame_nom = customtkinter.CTkButton(container, height=int(self.height*3/5), fg_color=theme_color,
                                            text="", hover_color=theme_color)
        frame_nom.grid(row=0, column=1, padx=10, sticky="nsew")
        frame_nom.grid_rowconfigure(0, weight=1)
        frame_nom.grid_columnconfigure(0, weight=1)
        frame_nom.grid_columnconfigure(1, weight=1)
        label_nom = customtkinter.CTkButton(frame_nom, text_color=label_color, fg_color=theme_color,
                                            hover_color=theme_color, text=self.nom.title(), anchor='w',
                                            font=customtkinter.CTkFont(family="Inter", size=20, weight="bold"), width=30)
        label_nom.grid(row=0, column=0, sticky="w")
        label_time = customtkinter.CTkButton(frame_nom, text_color=label_color, fg_color=theme_color, anchor='e',
                                             hover_color=theme_color, text="07:38", font=customtkinter.CTkFont(family="Inter", size=15, weight="bold"),
                                             width=10)
        label_time.grid(row=0, column=1, sticky='e')

        frame_msg = customtkinter.CTkButton(container, height=int(self.height*2/5), fg_color=theme_color,
                                            text="", hover_color=theme_color)
        frame_msg.grid(row=1, column=1, sticky="w")
        frame_msg.grid_rowconfigure(0, weight=1)
        frame_msg.grid_columnconfigure(0, weight=1)
        label_msg = customtkinter.CTkButton(frame_msg, text="je vais bien", text_color=msg_color, fg_color=theme_color,
                                            font=customtkinter.CTkFont(family="Inter", size=12), hover_color=theme_color, anchor='w',
                                            width=50)
        label_msg.grid(row=0, column=0, padx=9, sticky="w")


if __name__ == "__main__":
    app = App()
    app.mainloop()

