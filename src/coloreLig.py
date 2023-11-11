from coloriable2 import *
from CONSTANTES import *
from Grille import *
import copy

def coloreLig(A : Grille, i : int) -> (bool, Grille, set):
    ligneColors : list[int] = copy.deepcopy(A.grille[i])
    l : int = len(A.seqs_lig[i])
    Nouveaux : set = set()
    
    for z in range(A.M) :
        if (ligneColors[z]) == GRAY :
            # Test : case blanche
            memo : list[list[int]] = creationMemo(A.M, A.N)
            ligneColors[z] = WHITE
            testWhite = coloriable2(A.M - 1, l, A.seqs_lig[i], memo, ligneColors)
            
            # Test : case noire
            memo = creationMemo(A.M, A.N)
            ligneColors[z] = BLACK
            testBlack = coloriable2(A.M - 1, l, A.seqs_lig[i], memo, ligneColors)
            
            # Cas : Aucun test échoué, on ne peut rien déduire.
            if (testWhite and testBlack) :
                ligneColors[z] = GRAY
                A.grille[i][z] = GRAY
            
            # Cas : Test blanc réussi, on peut colorier la case en blanc.
            elif (testWhite and not testBlack) :
                ligneColors[z] = WHITE
                A.grille[i][z] = WHITE
                Nouveaux.add(z)
                
            # Cas : Test noir réussi, on peut colorier la case en noir.
            elif (not testWhite and testBlack) :
                ligneColors[z] = BLACK
                A.grille[i][z] = BLACK
                Nouveaux.add(z)
                
            # Cas : Aucun test réussi, le puzzle n'a pas de solution.
            else :
                return (False, A, Nouveaux)
    
    return (True, A, Nouveaux)
            
    