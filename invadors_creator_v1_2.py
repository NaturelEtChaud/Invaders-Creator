#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:20:40 2022

@author: loran
"""

from random import randint
from termcolor import colored, cprint

def invaders_creator(long,nb):
    '''
    Entéres :
        long est la longueur d'une ligne
        nb est le nombre de lignes
    
    '''
    # on remplit un tableau 2D de None aux bonnes dimensions
    tab = [[None for i in range(long)] for j in range(nb)]
    # on calcule la médiane
    mediane = round(long/2)
    # la troisième couleur
    couleur3 = randint(2,7)
    # on remplit chaque ligne en symétrique
    for j in range(nb):
        for i in range(mediane):
            couleur = randint(0,2)
            if couleur==2:
                val = couleur3
            else :
                val = couleur
            tab[j][i] = val
            tab[j][-i-1] = val
    return tab
    
def dessin_invader(tab):
    '''
    la fonction à faire évoluer à l'avennnnnnnir
    '''
    color = ['white','grey','red','green','yellow','blue','magenta','cyan']
    nb = len(tab)
    long = len(tab[0])
    dessin = ''
    for j in range(nb):       
        for i in range(long):
            num_color = tab[j][i]
            if num_color != 0:
                dessin = dessin + colored(' ',color[num_color],'on_'+color[num_color])
            else :
                dessin = dessin + ' '
        dessin = dessin + ('\n')
    print(dessin)
    
    
    
    
    
if __name__ == "__main__":
    invader = invaders_creator(11,9)
    dessin_invader(invader)
