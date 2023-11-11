from CONSTANTES import *

class Grille :
    """
        Classe représentant une grille.
    """
    def __init__(self, sequences_lignes : list[list[int]] = [], sequences_colonnes : list[list[int]] = []) :
        self.seqs_lig = sequences_lignes
        self.seqs_col = sequences_colonnes
        
        self.N : int = len(self.seqs_lig)
        self.M : int = len(self.seqs_col)
        self.grille : list[list[int]] = [[GRAY for _ in range(self.M)] for _ in range(self.N)]
        
        
    
    def coloriageTermine(self) -> bool :
        """
            Vérifie si la grille a été entièrement colorée.
        """
        for i in range(self.N) :
            for j in range(self.M) :
                if self.grille[i][j] == GRAY :
                    return False
        return True
    
    def afficheGrille(self) -> None :
        """
            Affiche la grille en tenant compte du coloriage.
        """

        for i in range(self.N) :
            for j in range(self.M) :
                case : int = self.grille[i][j]
                if(case == BLACK) :
                    print(u"\u25A0", end = '')
                elif(case == WHITE) :
                    print(u"\u25A1", end = '')  
                else :
                    print("+", end = '')
            print()
        print()