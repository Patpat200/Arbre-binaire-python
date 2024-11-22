
from arbre import*
from recherche import*

"""
********************************************************
*													   *
*			    Créé par Balqis & Adil                 *
*				  Terminal Genéral 6	        	   *
*													   *
********************************************************
"""


def minimum(T):
    """
    trouve le noeud avec la plus petite valeur dans un arbre binaire
    """
    while T.fils_gauche is not None:
        T = T.fils_gauche

    return T


def suppression(T,h):
    
    # regarde si l'arbre est vide ou pas
    if T is None:
        return None
    
    # si la valeur (h) à supprimer est plus petite que la racine actuel, on cherche à gauche
    if h < T.valeur:
        T.fils_gauche = suppression(T.fils_gauche, h)

    # si la valeur (h) est plus grande que le racine actuel, on cherche à droite
    elif h > T.valeur:
        T.fils_droit = suppression(T.fils_droit, h)

    # si la vaoeur est égal au neoud
    else:
        # est une feuille
        if T.fils_gauche is None and T.fils_droit is None:
            return None
        
        # un fils

        if T.fils_gauche is None:
            return T.fils_droit
        if T.fils_droit is None:
            return T.fils_gauche
        
        # a 2 fils, donc on cherche le successeur
        
        successeur = minimum(T.fils_droit)
        T.valeur = successeur.valeur  # remplace la valeur
        T.fils_droit = suppression(T.fils_droit, successeur.valeur)
    
    return T
        





t = Arbre(15)
t.setFilsDroit(18)
t.setFilsGauche(6)

t.getFilsGauche().setFilsGauche(3)
t.getFilsGauche().setFilsDroit(7)

t.getFilsDroit().setFilsDroit(20)
t.getFilsDroit().setFilsGauche(17)


print("avant la suppression")
print(Parcours_en_largeur(t))

print(suppression(t,17))

print("apres la suppression")
print(Parcours_en_largeur(t))








