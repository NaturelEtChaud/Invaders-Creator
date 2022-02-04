# Invaders-Creator

En tant que fan du Jeu [Space Invaders](https://fr.wikipedia.org/wiki/Space_Invaders) et de l'artiste [Invader](https://space-invaders.com/home/) je ne pouvais que moi-même m'y mettre

Voici mes 2 projets :
* Créer des *Invaders* en partant d'une moitié gauche par pixels aléatoires et en reproduisant la partie droite par symétrie </br>
Il devrait y avoir de nombreuses évolutions à cette partie du projet.
* Transformer une image en pixel art avec des Rubik's Cube comme le fait si bien [Invader](https://www.francetvinfo.fr/culture/arts-expos/street-art/la-joconde-en-rubik-s-cube-de-l-artiste-urbain-invader-s-envole-a-480-000-euros-aux-encheres_3839189.html)

---

# Projet 1 : Créer des personnages pour Space Invaders
* Une [première version](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/invadors_creator_v1_1.py) est disponible</br>
Elle permet de créer de manière aléatoire et par symétrie des `Invaders` dans la console.
* Evolution 1 : créer les `Invaders` au format `png` comme un assemblage de carrés du Rubik's Cube.
* Evolution 2 : créer un menu pour que l'utilisateur crée des `Invaders` jusqu'à ce qu'il obtienne un résultat satisfaisant.
* Evolution 3 : créer une base au format `txt` de tous les `Invaders` qui ont été créés et validés.
![](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/Invaders/invader0001.png)|
![](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/Invaders/invader0010.png)|![](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/Invaders/invader0100.png)|![](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/Invaders/invader1000.png)

---

# Projet 2 : Modifier une image pour obtenir une mosaique de Rubik's Cube
* Une [première version](https://github.com/NaturelEtChaud/Invaders-Creator/blob/main/rubiks_cube_v1.py) est disponible</br>
Elle permet de modifier une image en donnant la taille du carré du Rubik's Cube souhaité.
* Evolution 1 : créer une liste des images de référence du Rubik's Cube et pour les charger dès le départ pour ne pas avoir à charger la bonne image à chaque fois. Ceci devrait faire gagner un temps considérable à l'exécution du programme.
* Evolution 2 : ne plus utiliser les images, mais les dessiner, on devrait à nouveau pouvoir gagner du temps sur l'éxécution du programme.
* Evolution 3 : proposer l'option `gif animé`. (Pour le moment, j'ai effectué le `gif` à la main avec le logiciel GIMP une fois que j'ai récupéré toutes les images)
* Evolution 4 : tiens si j'ai vraiment du temps. Réécrire le script pour GIMP.

Voici ma trombine en Rubik's Cube :</br>
![](lo.gif)

