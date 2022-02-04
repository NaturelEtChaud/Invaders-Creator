#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:20:40 2022

@author: loran
"""

from random import randint
from termcolor import colored, cprint
from PIL import Image

def invaders_creator(long,nb):
    '''
    Entrées :
        long est la longueur d'une ligne
        nb est le nombre de lignes
    Sortie :
        un tableau 2D représentant l'invader en pixel art
        0 représente le noir (environ 40% des cases)
        1 représente le blanc (environ 50% des cases)
        2 à 6 représente une autre couleur (parmi celle du Rubik's cube)
    Rôle :
        créer un invader par symétrie 
    '''
    # on remplit un tableau 2D de None aux bonnes dimensions
    tab = [[None for i in range(long)] for j in range(nb)]
    # on calcule la médiane
    mediane = round(long/2)
    # la troisième couleur
    couleur3 = randint(2,6)
    # on remplit chaque ligne en symétrique
    for j in range(nb):
        for i in range(mediane):
            de_a_10 = randint(1,10)
            if de_a_10<=4 :
                # couleur noir
                val = 0
            elif de_a_10<=9 :
                # couelur blanche
                val = 1
            else :
                val = couleur3
            tab[j][i] = val
            tab[j][-i-1] = val
    return tab
    
def dessin_invader(tab):
    '''
    Entrée :
        le tableau 2D représentant l'Invader
    Sortie :
        None
    Rôle :
        Dessine dans la console l'Invader pour validation ou non
    Attention : 
        il n'y a pas d'orange dans la console, cette couleur est remplacée par du magenta.
    '''
    color = ['grey','white','blue','yellow','magenta','red','green']
    nb = len(tab)
    long = len(tab[0])
    dessin = ''
    for j in range(nb):       
        for i in range(long):
            num_color = tab[j][i]
            if num_color != 1:
                dessin = dessin + colored(' ',color[num_color],'on_'+color[num_color])
            else :
                dessin = dessin + ' '
        dessin = dessin + ('\n')
    print(dessin)
    
def image_invader(tab):
    '''
    Entrée :
        le tableau 2D représentant l'Invader
    Sortie :
        None
    Rôle :
        Dessine l'Invader dans une image au format png
        Chaque carré est un carré du Rubik's Cube
    '''
    # on charge toutes les images des carres.
    # attention, il n'y a pas de face noir on devra procéder à un décalage
    carres = ['blanc.png', 'bleu.png', 'jaune.png', 'orange.png', 'rouge.png', 'vert.png']
    images_carres = [Image.open('images/'+carres[i]) for i in range(6)]
    # on crée l'image support, elle est noire
    # il y aura un bord noir tout autour
    # l'unité de référence est 90 pixels, le côté d'un carré
    nb = len(tab)
    long = len(tab[0])
    largeur = (long+2)*90
    hauteur = (nb+2)*90
    support = Image.new ("RGB", (largeur, hauteur), "black")
    # on pose les carrés dans l'image support
    for j in range(nb):
        for i in range(long):
            num_color = tab[j][i]
            if num_color != 0: # sinon, c'ets noir, on ne fait rien
                # on colle l'image du carré
                for x in range(90):
                    for y in range(90):
                        R, V, B, opacite = images_carres[num_color-1].getpixel((x,y))
                        support.putpixel(((i+1)*90+x,(j+1)*90+y),(R,V,B))
    support.show()
    support.save('invader0000.png')

    
    
    
    
if __name__ == "__main__":
    invader = invaders_creator(11,9)
    print(invader)
    dessin_invader(invader)
    image_invader(invader)
