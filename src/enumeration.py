from indexNextCaseUndetermined import indexNextCaseUndetermined
from coloration import coloration
from enumRec import enumRec
from Grille import Grille
from CONSTANTES import *

def enumeration(A : Grille) :
    """
        Résout entièrement une grille donnée en paramètre.
    """
    
    ok, Ap = coloration(A)
    if ok != None :
        return (ok, Ap)
    
    k : int = indexNextCaseUndetermined(A, 0, 0)
    
    ok, Ap_1 = enumRec(Ap, k, WHITE)
    if ok != None :
        return (ok, Ap_1)
    
    ok, Ap_2 = enumRec(Ap, k, BLACK)
    if ok != None :
        return (ok, Ap_2)
    
    return (False, A)