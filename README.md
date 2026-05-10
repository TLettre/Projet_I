# Projet_I
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


## Documentation

Voici les différents documents qui se retrouvent dans le Github ainsi que la fonction de chacun.

[**Boitier**:](https://github.com/TLettre/Projet_I/blob/a2e4f342a44780944c0242c8f5481d343143d4d6/Boitier.zip)
Le fichier Boitier.zip contient les documents de la modélisation du boitier 3D. Tous les fichiers qui étaient nécessaires à l'impression se trouvent dans ce fichier.

[**Cahier des charges**:](https://github.com/TLettre/Projet_I/blob/81377b3d7a6bdb845bd9907a101511ad725f1cf8/Cahier_charges.docx)
Ce fichier contient toutes les informations concernant le projet: 
- Mise en situation et schéma de concept (p.3)
- Requis techniques et inconnus u projet (p.4-5)
- Livrables et échéancier (p.5-6)
Ce fichier regroupe donc toutes les informations que nous avions concernant le projet.

[**Schéma électrique**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_Circuit.SchDoc)
Ce fichier contien le schéma électrique du tableau de bord. 
- Le régulateur et la bobine ne sont pas les bonnes pièces.

[**PCB**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_PCB_2L.PcbDoc)
Fichier Altium du PCB complet du tableau de bord.
-  Les footprints de la bobine, du régulateur et des boutons ne sont pas les bonnes.

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
		
### Mode de fonctionnement
Les données ci-dessous devraient être visibles sur l'écran:
- Vitesse de la trottinette (en km/h)
- Pourcentage de la batterie
- Courrant consommé (en ampères)
- Température du système (en degrés celsius)
- État de l'éclairage (on ou off)
- Information de freinage (on ou off)

Lorsque la trottinette est en mode freinage, il est impossible d'accélérer.
		
[**Image du Dashboard en action**](https://github.com/TLettre/Projet_I/blob/main/Notes/dashboard%20trotinette.png)
