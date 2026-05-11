# Projet intégrateur 2: dashboard de trottinette
Projet Final de Projet Intégrateur 2.

## Mise en contexte

Le projet consiste à développer, programmer et assembler
un tableau de bord qui est fixé sur une trottinette électrique
complètement fonctionnelle à l’aide d’un boitier. Ce système 
électronique complet est supposé établir une communication avec le module
de contrôle, récupérer les données essentielles, traiter puis
présenter ces données ainsi que permettre au conducteur de visualiser
l’état du véhicule en temps réel.  

Dans ce fichier, il sera possible de voir la totalité des éléments présents autant en 
documentation que fonctionement au niveau du tableau de bord de la trottinette.


## Prérequis

### Matériel:
- Le PCB doit être alimenté avec 12V et 50mA.
- Le module de contrôle utilisé doit être le STM32U083CC.
- Le STM32U083CC doit être alimenté par un cable USB-C.
- Le dashboard doit être affiché sur un écran avec un cable USB-C à HDMI.
- Le PCB doit contenir un bouton de réinitialisation.
- Le branchement du connecteur JST qui est branché à la trottinette est définit dans le document de branchements.
- Nous avons ajouté des DELs d'alimentation pour chaque niveau d'alimentation, bien que ce requis était optionnel.
- Il doit y avoir 5mA maximum pour chaque DEL.
- Le PCB doit être fixé avec 4 vis M3.
- Nous avons fait la conception d’un boitier ergonomique pour encapsuler l’électronique, bien que ce requis soit optionnel.
- Le boitier doit pouvoir être bien fixé sur le guidon de la trottinette.
- Les dimmensions du PCB doivent être de 5cm par 5cm.
- Le PCB ne doit pas être accessible à l'usager.
- Les DELs d'alimentation ne doivent pas être accessibles à l'usager.
- Le boitier doit être simple à imprimer.

### Logiciel:
- Le module de contrôle et le tableau de bord doivent communiquer par protocole UART.
- Les données sont transmises par le module de contrôle dans un format JSON.
- Les informations suivantes doivent être affichées : la commande envoyée au moteur, la vitesse du véhicule, le pourcentage de charge de la batterie, le courant consommé, la température du système, l'état de l’éclairage, et l'information de freinage.
- L'affichage doit être ergonomique.
- L'information affichée doit être en temps réel.
- Le délai de rafraichissement doit être 4 fois par secondes.
- L'information affichée sur l'écran doit être épuré, clair, visible et compréhensible.

### Limitations:
- Nous ne connaissions pas l'ampleur du projet, ce qui a beaucoup affecté l'organisation de notre projet.

  
## Documentation

Voici les différents documents qui se retrouvent dans le Github ainsi que la fonction de chacun.


[**Boitier**:](https://github.com/TLettre/Projet_I/blob/a2e4f342a44780944c0242c8f5481d343143d4d6/Boitier.zip)
Le fichier Boitier.zip contient les documents de la modélisation du boitier 3D. Tous les fichiers qui étaient nécessaires à l'impression se trouvent dans ce fichier.


[**Cahier des charges**:](https://github.com/TLettre/Projet_I/blob/81377b3d7a6bdb845bd9907a101511ad725f1cf8/Cahier_charges.docx)
Ce fichier contient toutes les informations concernant le projet. 
- Mise en situation et schéma de concept (p.3)
- Requis techniques et inconnus u projet (p.4-5)
- Livrables et échéancier (p.5-6)
Ce fichier regroupe donc toutes les informations que nous avions concernant le projet.


[**Schéma bloc**:](https://github.com/TLettre/Projet_I/blob/feae1b3e02cbf4ebef9064a34becacfc2022ecb2/Notes/ProjetIntegrateur2.drawio)
Schéma qui explique le fonctionnement de notre PCB.


[**Schéma électrique**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_Circuit.SchDoc)
Ce fichier contien le schéma électrique du tableau de bord. 
- Le régulateur et la bobine ne sont pas les bonnes pièces.


[**PCB**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_PCB_2L.PcbDoc)
Fichier Altium du PCB complet du tableau de bord.
-  Les footprints de la bobine, du régulateur et des boutons ne sont pas les bonnes.


[**BOM**:](https://github.com/TLettre/Projet_I/blob/96cb56f76c8dbb2d10cd777ee212bbd68585368f/Altium/BOM.pdf)
Ce fichier contient les informations importantes de chacunes des pièces soudées sur le PCB.
-  La bobine et le régulateur ne sont pas les bonnes pièces et on été remplacées sur le PCB.


[**Code STM32**:](https://github.com/TLettre/Projet_I/blob/main/Code/code%20du%20stm32.c)
Code pour le fonctionnement du PCB.
- Il devrait prendre les données du fichier JSON et les envoyer vers le Raspberry Pi par UART.
- Des explications plus précises concernant le code se trouvent dans les commentaires du code.


[**Code Raspberry Pi**:](https://github.com/TLettre/Projet_I/blob/main/Code/code_pi.py)
Code qui permet de récupérer les donnés en JSON et de les envoyer sur l'écran.
- Des explications plus précises concernant le code se trouvent dans les commentaires du code.

Tout autre fichier de programmation sert à exécuter des tests.


## Guide d'utilisation

**Démarage**: Le tableau de bord devrait démarrer lorsque la trottinette est mise en marche.
		
### Mode de fonctionnement pour un utilisateur:
Les données ci-dessous devraient être visibles sur l'écran dès que la trottinette est activée:
- Vitesse de la trottinette (en km/h)
- Pourcentage de la batterie
- Courrant consommé (en ampères)
- Température du système (en degrés celsius)
- État de l'éclairage (on ou off)
- Information de freinage (on ou off)

Lorsque la trottinette est en mode freinage, il est impossible d'accélérer.
		
[**Image du Dashboard en action**](https://github.com/TLettre/Projet_I/blob/6009a4685d689ea0507f30d0aa41ed84b18c9245/Code/dashboard%20trotinette.png)

### Pour un développeur:
- La DEL D1 verte indique le fonctionnement du 12V.
- La DEL D2 rouge indique le fonctionnement 3.3V.
- Le bouton S1 permet de faire un RESET du PCB.
- Le bouton S2 permet de BOOTer le PCB pour envoyer un nouveau code dans le microcontrôleur.
