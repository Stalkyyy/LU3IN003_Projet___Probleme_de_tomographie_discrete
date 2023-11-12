from coloreLig import coloreLig
from coloreCol import coloreCol
from Grille import Grille
from CONSTANTES import *
import copy

def colorierEtPropager(A : Grille, i : int, j : int, c : int) :
    """
        Colore une grille A partiellement colorée. De plus, on commence par colorier la case (i,k) avec la couleur c.
    """
    
    Ap : Grille = copy.deepcopy(A)   # Pour ne pas modifier A en entrée
    LignesAVoir = [i]     # On ne prend que la ligne i
    ColonnesAVoir = [j]   # On ne prend que la colonne j
    
    # On colorie la case (i,j) avec la couleur c
    Ap.grille[i][j] = c
    
    while len(LignesAVoir) > 0 or len(ColonnesAVoir) > 0 :
        for i in LignesAVoir :
            ok, Ap, Nouveaux = coloreLig(Ap, i)
            if not ok :
                return (False, Grille())
            
            ColonnesAVoir = list(set(ColonnesAVoir) | Nouveaux)
            LignesAVoir.remove(i)
         
        for j in ColonnesAVoir :
            ok, Ap, Nouveaux = coloreCol(Ap, j)
            if not ok :
                return (False, Grille())
            LignesAVoir = list(set(LignesAVoir) | Nouveaux)
            ColonnesAVoir.remove(j)
        
    if Ap.coloriageTermine() :
        return (True, Ap)
    return (None, Ap)