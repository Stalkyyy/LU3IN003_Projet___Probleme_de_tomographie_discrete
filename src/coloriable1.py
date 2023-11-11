def coloriable1(j : int, l : int, s : list[int], memo : list[list[int]]) -> bool :
    """
        Renvoie vrai s'il est possible de colorier les j+1 premières cases (i,0), ..., (i,j) de la ligne l_i avec la sous-séquence (s_1, ..., s_l) des l premiers blocs de la ligne_i.
    
        Précondition : j = 0, ..., M-1 ; l = 1, ..., k; s[i] > 0 pour tout i, memo = matrice de taille M*k contenant les appels récursifs.
    """
        
    # On vérifie si on a déjà calculé T(j,l). Si c'est le cas, on renvoie directement sa valeur.
    if memo[j][l] != None :
        return memo[j][l]
    
    # Cas (1)
    elif (l == 0) :
        memo[j][l] = True
        
    # Cas (2a)
    elif (j < s[l-1] - 1) :
        memo[j][l] = False
        
    # Cas (2b)
    elif (j == s[l-1] - 1) :
        memo[j][l] = (l == 1)
    
    # Cas (2c)  
    else :
        memo[j][l] = coloriable1(j-1, l, s, memo) or coloriable1(j-s[l-1]-1, l-1, s, memo)
        
    return memo[j][l]