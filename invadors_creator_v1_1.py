#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 19:20:40 2022

@author: loran
"""

from random import randint

def invaders_creator(long,nb):
    '''
    Entrées :
        long est la longueur d'une ligne
        nb est le nombre de lignes
    
    '''
    # on remplit une tableau 2D de None aux bonnes dimensions
    tab = [[None for i in range(long)] for j in range(nb)]
    # on calcule la médiane
    mediane = round(long/2)
    # on remplit chaque ligne en symétrique
    for j in range(nb):
        for i in range(mediane):
            val = randint(0,1)
            tab[j][i] = val
            tab[j][-i-1] = val
    return tab
    
def dessin_invader(tab):
    '''
    la fonction à faire évoluer à l'avennnnnnnir
    '''
    nb = len(tab)
    long = len(tab[0])
    dessin = ''
    for j in range(nb):
        
        for i in range(long):
            if tab[j][i] == 1:
                dessin = dessin + chr(0x25A0)
            else :
                dessin = dessin + ' '
        dessin = dessin + ('\n')
    print(dessin)
    
    
    
    
    
if __name__ == "__main__":
    invader = invaders_creator(11,9)
    dessin_invader(invader)
