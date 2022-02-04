from PIL import Image

def plus_proche(R,V,B):
    '''
    Entrées 
        R, V, B pour les composantes Rouge, Verte et Bleu d'un pixel
    Sortie 
        la couleur du rubiks cube la plus proche parmi blanc, bleu, jaune, orange, rouge, vert
    Rôle
        renvoie le nom de la couleur la plus proche du triplet (R,V,B)
    '''
    etiquettes = {'blanc' : (255,255,255), 'bleu' : (0,69,173), 'jaune' : (255,213,0), 'orange' : (255,88,0), 'rouge' : (183,18,52), 'vert' : (0,154,72)}
    distance = 444 # distance supérieure à toute distances possibles
    couleur = ''
    for nom, triplet in etiquettes.items():
        nouvelle_distance = ((R-triplet[0])**2 + (V-triplet[1])**2 + (B-triplet[2])**2)**0.5
        if nouvelle_distance < distance :
            distance = nouvelle_distance
            couleur = nom
    return couleur

def pixel_moyen(img, x, y, cote):
    '''
    Entrées
        img est l'objet PIL image
        x et y sont les coordonénes du coin en haut à gauche du carré considéré
        cote est la longueur du côté du carré
    Sortie
        un triplet R, V, B
    Rôle
        renvoie la composante Rouge, Verte et Bleu moyenne de tous les pixesl du carré
    '''
    largeur, hauteur = img.size
    #calcul de la couleur moyenne
    Rsom, Vsom, Bsom = 0, 0, 0
    nb_pixels = 0
    for i in range(x,x+cote):
        for j in range (y,y+cote):
            #il ne faut pas déborder
            if i<largeur and j<hauteur :
                R, V, B = img.getpixel((i,j))
                Rsom += R
                Vsom += V
                Bsom += B
                nb_pixels += 1
    Rmoy = Rsom // nb_pixels
    Vmoy = Vsom // nb_pixels
    Bmoy = Bsom // nb_pixels
    return Rmoy, Vmoy, Bmoy

def remplir(img, x, y, cote, couleur):
    '''
    Entrées
        img est l'image à modifier
        x et y sont les coordonnées du coin en haut à gauche du carré
        cote est la longueur du côté du carré
        couleur est la couleur du rubik's cube que l'on va choisir
    Sortie
        None
    Rôle
        va remplir le carré de coin enhaut à gauche (x,y) avec l'image d'une vignette du rubik's cube
    '''
    largeur, hauteur = img.size
    vignette = Image.open('images/'+couleur+'.png')
    lar, haut = vignette.size
    pas = lar//cote
    for i in range(cote):
        for j in range(cote):
            if x+i < largeur and y+j< hauteur :
                R, V, B, opacite = vignette.getpixel((i*pas,j*pas))
                img.putpixel((x+i,y+j),(R,V,B))


def rubik_cube(nomimage, cote, nomdestination):
    '''
    Entrées :
        nomimage est le nom de l'image complet (avec son extension)
        cote est la taille en pixel du coté du carré de la mosaïque
        nomdestination est le nom pour le résultat
    Sorite :
        None
    Rôle :
        Reconstruire l'image en mosaïque de rubik's cube
    '''
    img = Image.open('images/'+nomimage)
    largeur, hauteur = img.size
    for x in range(0,largeur,cote):
        for y in range(0,hauteur,cote):
            Rmoy, Vmoy, Bmoy = pixel_moyen(img, x, y, cote)
            couleur_rubik = plus_proche(Rmoy, Vmoy, Bmoy)
            remplir(img, x, y, cote, couleur_rubik)
    img.show()
    img.save(nomdestination)
