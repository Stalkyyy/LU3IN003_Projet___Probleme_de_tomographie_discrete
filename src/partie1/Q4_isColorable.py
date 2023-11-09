def isColorable(j : int, l : int, s : list[int], memo : list[list[int]] = None) -> bool :
    """
        Renvoie vrai s'il est possible de colorier les j+1 premières cases (i,0), ..., (i,j) de la ligne l_i avec la sous-séquence (s_1, ..., s_l) des l premiers blocs de la ligne_i.
    
        Précondition : j = 0, ..., M-1 ; l = 1, ..., k; s[i] > 0 pour tout i, memo = None.
    """
    
    # Si c'est la premier appel à la fonction, on crée une matrice afin de sauvegarder en mémoire les résultats des appels récursifs.
    if memo == None :
        memo = [[None] * (l+1) for _ in range(j+1)]
        
    # On vérifie si on a déjà calculé T(j,l). Si c'est le cas, on renvoie directement sa valeur.
    if memo[j][l] != None :
        return memo[j][l]
    
    # Cas (1)
    if (l == 0) :
        memo[j][l] = True
        return True
        
    # Cas (2a)
    if (j < s[l-1] - 1) :
        memo[j][l] = False
        
    # Cas (2b)
    elif (j == s[l-1] - 1) :
        if (l == 1) :
            memo[j][l] = True
        else :
            memo[j][l] = False
    
    # Cas (2c)  
    else :
        memo[j][l] = isColorable(j-1, l, s, memo) or isColorable(j-s[l-1]-1, l-1, s, memo)
        
    return memo[j][l]


# PS : On retourne la valeur exceptionnellement au cas 1 pour éviter l'erreur => IndexError : list index out of range, dans le cas où l = 0.