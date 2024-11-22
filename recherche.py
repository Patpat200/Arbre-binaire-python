def Recherche_valeur_rec(T,k):
    """regarde si la veleur est dedans"""
    if T == None:
        return False
    
    x = T
    
    if k == x.valeur:
        return True
    
    if k < x.valeur:
        return Recherche_valeur_rec(x.fils_gauche, k)
        
    else:
        return Recherche_valeur_rec(x.fils_droit, k)



def Recherche_valeur_ite(T,k):
    """trouve la clé de la valeur"""
    x = T
    while T != None and k != x.valeur:
        
        
        if k < x.valeur:
            T = x.fils_gauche
        
        else:
            T = x.fils_droit

        x = T
        
    if T == None:
        return False
    
    else:
        return True



def insert_arbre(T,y):
    
    x = T
    
    while T != None:
        x = T
        if y < x.valeur:
            T = x.fils_gauche
        
        else:
            T = x.fils_droit
        
    if y < x.valeur:
        x.setFilsGauche(y)

    else:
        x.setFilsDroit(y)
    