from Grille import Grille
from CONSTANTES import *

def indexNextCaseUndetermined(A : Grille, i : int, j : int) :
    """
        Recherche l'indice k de la prochaine case de couleur indéfinie.
    """
    for x in range(i, A.N) :
        for y in range(j, A.M) :
            if A.grille[x][y] == GRAY :
                return A.M * x + y
    return A.M * A.N