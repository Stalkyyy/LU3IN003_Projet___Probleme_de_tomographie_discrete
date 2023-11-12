from CONSTANTES import *

def coloriable2(j : int, l : int, s : list[int], memo : list[list[int]], colors : list[int]) -> bool :
    """
        Forme améliorée de isColorable où on vérifie si une case est déjà coloriée en amont.
    
        Précondition : j = 0, ..., M-1 ; l = 1, ..., k; s[i] > 0 pour tout i, memo = matrice de taille M*k contenant les appels récursifs, colors = tableau de taille M contenant la couleur potentielle de chaque case.
    """
        
    # On vérifie si on a déjà calculé T(j,l). Si c'est le cas, on renvoie directement sa valeur.
    if memo[j][l] != UNDEFINED :
        return memo[j][l]
    
    # Cas (1)
    if (l == 0) :
        memo[j][l] = containsNoXColor(0, j, BLACK, colors)
        return memo[j][l]

    # Cas (2a)
    if (j < s[l-1] - 1) :
        memo[j][l] = False
        
    # Cas (2b)
    elif (j == s[l-1] - 1) :
        memo[j][l] = ((l == 1) and containsNoXColor(0, j, WHITE, colors))
    
    # Cas (2c)  
    else :
        memo[j][l] = False
        
        # Test : possibilité de la case blanche, on la retourne directement si c'est vrai, pour ne pas à avoir à tester le cas noir (OU LOGIQUE).
        if colors[j] != BLACK :
            memo[j][l] = coloriable2(j-1, l, s, memo, colors)
            if memo[j][l] :
                return True
        
        # Test : possibilité de la case noire.
        if colors[j] != WHITE :
            memo[j][l] = colors[j-s[l-1]] != BLACK and coloriable2(j-s[l-1]-1, l-1, s, memo, colors)  and containsNoXColor(j-s[l-1]+1, j, WHITE, colors)
            
    return memo[j][l]



def containsNoXColor(min : int, max : int, color : int, colors : list[int]) :
    """
        Vérifie les cases (i,min), (i,min+1), ..., (i,max). Si une d'entre elle a la couleur passée en paramètre, renvoie False. Sinon True.
    """
    for i in range(min, max+1) :
        if colors[i] == color :
            return False
    return True