from lectureInstance import *
from coloration import *
from Grille import *


def propagation(path : str) :
    """
        Résout partiellement une grille représentée par son instance, dont le chemin est donné en paramètre.
    """
    
    A = lectureInstance(path)
    ok, A2 = coloration(A)
    
    if ok == None :
        print("On ne peut rien déduire.")
    elif ok == False :
        print("Le puzzle n'a pas de solution.")
    else :
        A2.afficheGrille()