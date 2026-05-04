#installer la librarie custom tkinter
#installer python 3 avant dans l'invite de commande du rasberry pi
#procedure installer lib pour rasberry

#python3 -m venv venv
#source venv/bin/activate
#pip install customtkinter
#pip install pyserial
# les 2 autres librairie sont déja disponible

import customtkinter as ctk
import json
import serial
# a voir pour la connexion avec la carte
#port = serial.Serial("COM3", baudrate=115200, timeout=1)
#def lecture_uart(port):

    #donees1 = port.readline()
    #données2 = donees1.decode("utf-8").strip()
    #donnees_utile = json.loads(données2)

    #return donnees_utile

def lire_donnees_test():
    with open("donnees_test.json", "r", encoding="utf-8") as fichier:
        return json.load(fichier)


def utilisation_donnees(donnees_utile):
    ctrl = donnees_utile["ctrl"]
    drive = donnees_utile["drive"]

    frein = ctrl["break_active"]
    estop = ctrl["estop_active"]
    moteur_on = ctrl["enable_active"]
    eclairage = ctrl["light_active"]
    commande = ctrl["cmd"]

    temperature = drive["temperature"]
    batterie = drive["battery_percentage"]
    courant = drive["motor_current"]
    vitesse = drive["speed"]

    return {
        "frein": frein,
        "estop": estop,
        "moteur_on": moteur_on,
        "eclairage": eclairage,
        "commande": commande,
        "temperature": temperature,
        "batterie": batterie,
        "courant": courant,
        "vitesse": vitesse,
    }


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("dashboard_trotinette")
        self.configure(fg_color="#0d1117")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_drive = InfoConduite(self, fg_color="#161b22")
        self.frame_drive.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
        self.mettre_a_jour_test()

    def mettre_a_jour_test(self):
        self.frame_drive.mettre_a_jour_affichage(lire_donnees_test())
        self.after(1000, self.mettre_a_jour_test)


class InfoConduite(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        for row in range(1, 6):
            self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(0, weight=0, minsize=230)
        self.grid_columnconfigure(1, weight=1)

        self.titre = ctk.CTkLabel(
            self,
            text="INFO TROTTINETTE",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="white",
        )
        self.titre.grid(row=0, column=0, columnspan=2, pady=(22, 12), sticky="n")

        self.case_batterie = CaseInfo(self, "Batterie", "%")
        self.case_temperature = CaseInfo(self, "Temperature", "C")
        self.case_vitesse = CaseInfo(self, "Vitesse", "km/h")
        self.case_courant = CaseInfo(self, "Courant", "A")
        self.case_commande = CaseInfo(self, "Commande", "cmd")

        self.case_batterie.grid(row=1, column=1, padx=(25, 45), pady=14, sticky="nsew")
        self.case_temperature.grid(row=2, column=1, padx=(25, 45), pady=14, sticky="nsew")
        self.case_vitesse.grid(row=3, column=1, padx=(25, 45), pady=14, sticky="nsew")
        self.case_courant.grid(row=4, column=1, padx=(25, 45), pady=14, sticky="nsew")
        self.case_commande.grid(row=5, column=1, padx=(25, 45), pady=14, sticky="nsew")

        self.case_frein = CaseOnOff(self, "Freinage")
        self.case_eclairage = CaseOnOff(self, "Eclairage")
        self.case_moteur = CaseOnOff(self, "Moteur")
        self.case_estop = CaseOnOff(self, "Arret urgence")

        self.case_frein.grid(row=1, column=0, padx=(35, 15), pady=14, sticky="n")
        self.case_eclairage.grid(row=2, column=0, padx=(35, 15), pady=14, sticky="n")
        self.case_moteur.grid(row=3, column=0, padx=(35, 15), pady=14, sticky="n")
        self.case_estop.grid(row=4, column=0, padx=(35, 15), pady=14, sticky="n")

    def mettre_a_jour_affichage(self, donnees_utile):
        donnees = utilisation_donnees(donnees_utile)

        self.case_frein.mettre_a_jour(donnees["frein"])
        self.case_eclairage.mettre_a_jour(donnees["eclairage"])
        self.case_moteur.mettre_a_jour(donnees["moteur_on"])
        self.case_estop.mettre_a_jour(donnees["estop"])

        self.case_vitesse.mettre_a_jour(donnees["vitesse"])
        self.case_temperature.mettre_a_jour(donnees["temperature"])
        self.case_batterie.mettre_a_jour(donnees["batterie"])
        self.case_courant.mettre_a_jour(donnees["courant"])
        self.case_commande.mettre_a_jour(donnees["commande"])


class CaseOnOff(ctk.CTkFrame):
    def __init__(self, master, titre, **kwargs):
        super().__init__(
            master,
            width=185,
            height=105,
            corner_radius=10,
            border_width=1,
            border_color="#2d3748",
            fg_color="#1a202c",
            **kwargs,
        )
        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text=titre.upper(),
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#718096",
        ).pack(pady=(10, 2))

        self.label_pastille = ctk.CTkLabel(
            self,
            text="●",
            font=ctk.CTkFont(size=24),
            text_color="#4a5568",
        )
        self.label_pastille.pack()

        self.label_etat = ctk.CTkLabel(
            self,
            text="INACTIF",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#4a5568",
        )
        self.label_etat.pack(pady=(0, 10))

    def mettre_a_jour(
        self,
        actif,
        texte_on="ACTIF",
        texte_off="INACTIF",
        couleur_on="#22c55e",
        couleur_off="#4a5568",
    ):
        couleur = couleur_on if actif else couleur_off
        texte = texte_on if actif else texte_off
        self.label_pastille.configure(text_color=couleur)
        self.label_etat.configure(text=texte, text_color=couleur)


class CaseInfo(ctk.CTkFrame):
    def __init__(self, master, titre, unite="", **kwargs):
        super().__init__(
            master,
            corner_radius=10,
            border_width=1,
            border_color="#2d3748",
            fg_color="#1a202c",
            **kwargs,
        )

        ctk.CTkLabel(
            self,
            text=titre.upper(),
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#718096",
        ).pack(pady=(16, 4))

        self.label_valeur = ctk.CTkLabel(
            self,
            text="--",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white",
        )
        self.label_valeur.pack()

        ctk.CTkLabel(
            self,
            text=unite,
            font=ctk.CTkFont(size=11),
            text_color="#718096",
        ).pack(pady=(4, 16))

    def mettre_a_jour(self, nouvelle_valeur, couleur="white"):
        self.label_valeur.configure(text=str(nouvelle_valeur), text_color=couleur)


app = App()
app.mainloop()
