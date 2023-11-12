from coloriable2 import coloriable2
from Grille import Grille
from CONSTANTES import *

def coloreCol(A : Grille, i : int) -> (bool, Grille, set):
    colonneColors : list[int] = [ligne[i] for ligne in A.grille]
    l : int = len(A.seqs_col[i])
    Nouveaux : set = set()
    
    for z in range(A.N) :
        if colonneColors[z] == GRAY :
            # Test : case blanche
            memo : list[list[int]] = creationMemo(A.N, A.M)
            colonneColors[z] = WHITE
            testWhite = coloriable2(A.N - 1, l, A.seqs_col[i], memo, colonneColors)
            
            # Test : case noire
            memo : list[list[int]] = creationMemo(A.N, A.M)
            colonneColors[z] = BLACK
            testBlack = coloriable2(A.N - 1, l, A.seqs_col[i], memo, colonneColors)
            
            # Cas : Aucun test échoué, on ne peut rien déduire.
            if (testWhite and testBlack) :
                colonneColors[z] = GRAY
                A.grille[z][i] = GRAY
            
            # Cas : Test blanc réussi, on peut colorier la case en blanc.
            elif (testWhite and not testBlack) :
                colonneColors[z] = WHITE
                A.grille[z][i] = WHITE
                Nouveaux.add(z)
                
            # Cas : Test noir réussi, on peut colorier la case en noir.
            elif (not testWhite and testBlack) :
                colonneColors[z] = BLACK
                A.grille[z][i] = BLACK
                Nouveaux.add(z)
                
            # Cas : Aucun test réussi, le puzzle n'a pas de solution.
            else :
                return (False, A, Nouveaux)
    
    return (True, A, Nouveaux)
            