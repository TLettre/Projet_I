import customtkinter as ctk
import serial
import json


#port = serial.Serial("COM3", baudrate=115200, timeout=1)
def lecture_uart(port):

    donees1 = port.readline()
    données2 = donees1.decode("utf-8").strip()
    donnees_utile = json.loads(données2)

    return donnees_utile

def utilisation_donnes(donnees_utile):
    ctrl  = donnees_utile["ctrl"]
    drive = donnees_utile["drive"]

# Ensuite, lire chaque valeur dedans
    etat        = ctrl["state"]             # → "INIT"
    frein       = ctrl["break_active"]      # → "false"  
    estop       = ctrl["estop_active"]      # → "false" 
    moteur_on   = ctrl["enable_active"]     # → "false"
    eclairage   = ctrl["light_active"]      # → "false"
    
    fault       = ctrl["fault_code"]        # → "none"
    commande    = ctrl["cmd"]               # → 0

    temperature = drive["temperature"]        # → 25.49
    batterie    = drive["battery_percentage"] # → 80.0
    courant     = drive["motor_current"]      # → 200.5
    mode        = drive["motor_mode"]         # → "turtle"
    vitesse     = drive["speed"]
    return { "etat": etat, "frein": frein, "estop": estop,
        "moteur_on": moteur_on, "eclairage": eclairage,
        "fault": fault, "commande": commande,
        "temperature": temperature, "batterie": batterie,
        "courant": courant, "mode": mode, "vitesse": vitesse,}

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x1000")
        self.title("projet_1")
        self.configure(fg_color="#0d1117")
 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
 
        # Le frame principal avec toutes les cases
        self.frame_drive = info_conduite(self, fg_color="#161b22",)
        self.frame_drive.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

class info_conduite(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        ctk.CTkLabel(self,text="info trotinette",text_color="white")
        self.case_vitesse     = CaseInfo(self, "Vitesse",     "km/h")
        self.case_temperature = CaseInfo(self, "Temperature", "C")
        self.case_batterie    = CaseInfo(self, "Batterie",    "%")
        self.case_courant     = CaseInfo(self, "Courant",     "A")
        self.case_commande    = CaseInfo(self, "Commande",    "cmd")
 
    
        self.case_vitesse.grid(    row=3, column=2, padx=8, pady=8, sticky="nsew")
        self.case_temperature.grid(row=2, column=2, padx=8, pady=8, sticky="nsew")
        self.case_batterie.grid(   row=1, column=2, padx=8, pady=8, sticky="nsew")
        self.case_courant.grid(    row=4, column=2, padx=8, pady=8, sticky="nsew")
        self.case_commande.grid(   row=5, column=2, padx=8, pady=8, sticky="nsew")
 
        # ── Ligne 2 : etats ON/OFF ─────────────────────────────
        self.case_frein     = CaseOnOff(self, "Freinage")
        self.case_eclairage = CaseOnOff(self, "Eclairage")
        self.case_moteur    = CaseOnOff(self, "Moteur")
        self.case_estop     = CaseOnOff(self, "Arret urgence")
 
        self.case_frein.grid(    row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.case_eclairage.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.case_moteur.grid(   row=3, column=0, padx=5, pady=5, sticky="nsew")
        self.case_estop.grid(    row=4, column=0, padx=5, pady=5, sticky="nsew") 
 
        # ── Ligne 3 : textes (etat, mode, fault) ──────────────
        self.case_etat  = CaseInfo(self, "Etat ctrl",   "")
        self.case_mode  = CaseInfo(self, "Mode moteur", "")
        self.case_fault = CaseInfo(self, "Fault code",  "")
 
        self.case_etat.grid( row=1, column=4, padx=8, pady=8, sticky="nsew")
        self.case_mode.grid( row=2, column=4, padx=8, pady=8, sticky="nsew")
        self.case_fault.grid(row=3, column=4, padx=8, pady=8, sticky="nsew")
 
        # Rendre les colonnes de taille egale
        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
class CaseOnOff(ctk.CTkFrame):
  
    def __init__(self, master, titre, **kwargs):
        super().__init__(master, corner_radius=10, border_width=1,
                         border_color="#2d3748", fg_color="#1a202c", **kwargs)
 
        ctk.CTkLabel(
            self,
            text=titre.upper(),
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#718096",
        ).pack(pady=(10, 4))
 
        # Pastille ronde (simulee avec un gros "bullet")
        self.label_pastille = ctk.CTkLabel(
            self,
            text="●",
            font=ctk.CTkFont(size=30),
            text_color="#4a5568",  # gris = inactif
        )
        self.label_pastille.pack()
 
        self.label_etat = ctk.CTkLabel(
            self,
            text="INACTIF",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#4a5568",
        )
        self.label_etat.pack(pady=(2, 10))
 
    def mettre_a_jour(self, actif, texte_on="ACTIF", texte_off="INACTIF",
                       couleur_on="#22c55e", couleur_off="#4a5568"):
  
        
        couleur = couleur_on if actif else couleur_off
        texte   = texte_on   if actif else texte_off
        self.label_pastille.configure(text_color=couleur)
        self.label_etat.configure(text=texte, text_color=couleur)
           
class CaseInfo(ctk.CTkFrame):
  
    def __init__(self, master, titre, unite="", **kwargs):
        super().__init__(master, corner_radius=10, border_width=1,
                         border_color="#2d3748", fg_color="#1a202c", **kwargs)
 
        # Titre en haut
        ctk.CTkLabel(
            self,
            text=titre.upper(),
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#718096",
        ).pack(pady=(10, 2))
 
        # Valeur au milieu (grande)
        self.label_valeur = ctk.CTkLabel(
            self,
            text="--",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white",
        )
        self.label_valeur.pack()
 
        # Unite en bas
        ctk.CTkLabel(
            self,
            text=unite,
            font=ctk.CTkFont(size=11),
            text_color="#718096",
        ).pack(pady=(2, 10))

    
 
    def mettre_a_jour(self, nouvelle_valeur, couleur="white"):
       
        self.label_valeur.configure(text=str(nouvelle_valeur), text_color=couleur)
      


app = App()
app.mainloop()
