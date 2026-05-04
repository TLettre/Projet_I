# Projet_I
Projet Final de Projet Intégrateur 2.

## Mise en contexte

Le project consiste à développer, programmer et assembler
un tableau de bord qui est fixée sur une trottinette électrique
complètement fonctionnelle, à l’aide d’un boitier. Ce système 
électronique complet est suposer établir une communication avec le module
de contrôle, récupérer les données essentielles, traiter puis
présenter ces données ainsi que permettre au conducteur visualiser
l’état du véhicule en temps réel.  

dans ce fichier, il sera possible de voir la totalité des élément présent autant en 
documentation que fonctionement au niveau du tableau de bord de la trotinette.


## documentation

Voici les différents documents qui se retrouvent dans le Github ainsi que la fonction de chacun.

[**Boitier**:](https://github.com/TLettre/Projet_I/blob/a2e4f342a44780944c0242c8f5481d343143d4d6/Boitier.zip)
Le fichier Boitier.zip contient les documents de la modélisation du boitier 3D. Tous les fichiers qui étaient nécessaires à l'impression se retrouvent dans ce fichier.

[**Cahier des charges**:](https://github.com/TLettre/Projet_I/blob/81377b3d7a6bdb845bd9907a101511ad725f1cf8/Cahier_charges.docx)
Ce fichier contient toutes les informations concernant le projet: 
- Mise en situation et schéma de concept (p.3)
- Requis techniques et inconnus (p.4-5)
- Livrables et échéancier (p.5-6)
Ce fichier regroupe donc toutes les informations que nous avions concernant le projet.

[**Schéma électrique**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_Circuit.SchDoc)
Le fichier contien le schéma électrique du tableau de bord. 
- Le régulateur et la Bobine ne sont pas les bonne pièce.

[**PCB**:](https://github.com/TLettre/Projet_I/blob/main/Altium/PI2_PCB_2L.PcbDoc)
Fichier du PCB complet du tableau de bord.
-La footprint de la bobine, du régulateur et des bouton ne sont pas les bonne.

## Guide d'utilisation

Démarage
	Le tableau de bord devrait démarrer lorsque la trotinette est mise en marche.
		
### Mode de fonctionnement
Les données ci dessous devraient être visibles sur l'écran:
- Vitesse de la trotinette
- Pourcentage de la batterie
- Courrant consommé
- Température du système
- État de l'éclairage
- information de freinage
- lorsque la trotinette est en mode freinage, il est impossible d'accélérer.
		
			
		
