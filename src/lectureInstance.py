from Grille import Grille

def lectureInstance(path : str) :
    """
        Lit un fichier texte dont chaque ligne correspond à la séquence associée à une ligne ou une colonne de la grille.
        Le symbole # indique que l'on passe à la description des lignes à celle des colonnes.
        Avant le #, il y a autant de lignes dans le fichier que de lignes dans la grille, et à chaque ligne est indiquée la séquence d'entiers représentant les longueurs de blocs.
        
        La fonction renvoie le grille correspondante ainsi qu'un tableau comportant les séquences lignes, et un autre tableau comportant les séquences colonnes.
    """
    # Pour commenter le code, on utilisera l'instance 0.txt comme exemple.
    
    # Lis le fichier, fileRead est un tableau de forme : ['3', '', '1 1 1', '3', '#', '1 1', '1', '1 2', '1', '2'].
    with open(path, 'r') as fp :
        fileRead : list[str] = [line.strip('\n') for line in fp.readlines()]
    
    # On trouve l'index du séparateur '#' afin de découper en deux le tableau. Un pour les séquences des lignes, et l'autre pour les séquences des colonnes.
    index_separator_lig_col : int = fileRead.index("#")
    seqs_lig : list[str] = fileRead[:index_separator_lig_col]
    seqs_col : list[str] = fileRead[index_separator_lig_col+1:]
    
    # Nous créons une liste finale comportant les séquences sous forme de liste de int.
    # On aura donc pour les lignes, [[3], [], [1, 1, 1], [3]]
    # On aura donc pour les colonnes, [[1, 1], [1], [1, 2], [1], [2]]
    seqs_lig : list[list[int]] = [list(map(int, sequence.split(' '))) if sequence else [] for sequence in seqs_lig]
    seqs_col : list[list[int]] = [list(map(int, sequence.split(' '))) if sequence else [] for sequence in seqs_col]

    # Création d'une classe Grille.   
    return Grille(seqs_lig, seqs_col)