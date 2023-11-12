from indexNextCaseUndetermined import indexNextCaseUndetermined
from colorierEtPropager import colorierEtPropager
from Grille import Grille
from CONSTANTES import *

def enumRec(A : Grille, k : int, c : int) :
    """
        Fonction récursive où l'on colorie chaque case de couleur gris (indéfini) par la couleur blanche, puis noire.
        Cela permet de vérifier chaque cas possible et donc de colorier la totalité de la grille si possible.
    """
    
    # Cas de base : toutes les cases de A sont coloriées.
    if k == A.M * A.N :
        return (True, A)
    
    i : int = k // A.M
    j : int = k % A.M
    
    ok, Ap = colorierEtPropager(A, i, j, c)
    if ok != None :
        return (ok, Ap)
    
    # Indice de la prochaine case indéterminée à partir de k+1
    kp : int = indexNextCaseUndetermined(A, i, j)
    
    ok, Ap_1 = enumRec(Ap, kp, WHITE)
    if ok :
        return (ok, Ap_1)
    
    ok, Ap_2 = enumRec(Ap, kp, BLACK)
    if ok :
        return (ok, Ap_2)
    
    return (False, A)