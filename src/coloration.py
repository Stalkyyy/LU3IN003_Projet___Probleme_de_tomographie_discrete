from CONSTANTES import *
from coloreLig import *
from coloreCol import *
from Grille import *
import copy

def coloration(A : Grille) :
    """
        Colore une grille A entièrement non coloriée.
    """
    
    Ap : Grille = copy.deepcopy(A)   # Pour ne pas modifier A en entrée
    LignesAVoir = [i for i in range(Ap.N)]
    ColonnesAVoir = [i for i in range(Ap.M)]
    
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