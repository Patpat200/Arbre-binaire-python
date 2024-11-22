
from file import*

class Arbre:
    
    def __init__(self, valeur):
        self.valeur = valeur
        self.fils_gauche = None
        self.fils_droit = None
    
    def getValeur(self):
        return self.valeur
    
    def getFilsGauche(self):
        return self.fils_gauche
    
    def getFilsDroit(self):
        return self.fils_droit

    
    def setValeur(self, e):
        self.valeur = e
    
    def setFilsGauche(self, e):
        self.fils_gauche = Arbre(e)

    def setFilsDroit(self, e):
        self.fils_droit = Arbre(e)

    
    # Exercice 2
    def taille(self):
        
        ## nombre de noeux

        total = 1
        
        for fils in (self.fils_gauche, self.fils_droit):
            if fils is not None:
                total = total + fils.taille()
        
        return total
        
    
    ### AUTRE METHODE
    
    # def taille(self):
    #     # Calcul récursif de la taille
    #     taille_gauche = self.fils_gauche.taille() if self.fils_gauche else 0
    #     taille_droite = self.fils_droit.taille() if self.fils_droit else 0
    #     return 1 + taille_gauche + taille_droite
    
    
    def hauteur(self):  
        
        if self.valeur == None:
            return 0
        
        elif self.fils_gauche == None and self.fils_droit == None:
            return 1
        
        elif self.fils_gauche == None:
            return 1 + self.fils_droit.hauteur()
        
        elif self.fils_droit == None:
            return 1 + self.fils_gauche.hauteur()
        
        else:
            return 1 + max(self.fils_droit.hauteur(), self.fils_gauche.hauteur())
        
        
        

        

    ### EXERCICE 2
    




    

    
def Parcours_prefixe(T):
    
    if T != None:
        print(T.valeur)
            
        T.Parcours_prefixe(T.fils_gauche)
        T.Parcours_prefixe(T.fils_droit)
            

def Parcours_postfixe(T):
    if T != None:
           
        T.Parcours_postfixe(T.fils_gauche)
        T.Parcours_postfixe(T.fils_droit)
        print(T.valeur)
        
        
           
        
def Parcours_infixe(T):
    if T != None:
        
        T.Parcours_infixe(T.fils_gauche)
        print(T.valeur)
        T.Parcours_infixe(T.fils_droit)

    
def Parcours_en_largeur(T):
    f = File()
      
    f.enfiler(T)
        
    while not f.estVide():
        
        x = f.sommet()
        print(x.valeur)
        f.defiler()
                     
        if x.fils_gauche != None:
                
            f.enfiler(x.fils_gauche)
                
        if x.fils_droit != None:

            f.enfiler(x.fils_droit)





