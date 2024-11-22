

class File:
    """
    tete a droite queue a gauche
    """
    
    def __init__(self):
        self.files = []
    
    
    def estVide(self):
        if len(self.files) == 0:
            return True
        else:
            return False
    
    def enfiler(self, el):
        self.files = [el] + self.files
        return True
        
    def defiler(self):
        if self.estVide():
            return False
        else:
            self.files.pop()
            return True
    
    def sommet(self):
        if self.estVide():
            return None
        else:
            return self.files[-1]
        
    def taille(self):
        return len(self.files)
        
        
    
    