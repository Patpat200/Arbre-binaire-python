

# **Projet : Suppression dans un Arbre Binaire de Recherche**

## **Description**
Ce projet implémente la gestion de la suppression d'un nœud dans un arbre binaire de recherche (ABR). L'objectif est de maintenir les propriétés de l'arbre binaire de recherche après la suppression.  

L'arbre permet :
- L'insertion de valeurs
- La recherche de valeurs
- La suppression de valeurs

---

## **Structure du Projet**

### **Classes Principales**
1. **`Arbre`**  
   Représente un nœud d'un arbre binaire. Chaque nœud contient :
   - Une valeur
   - Un pointeur vers un fils gauche
   - Un pointeur vers un fils droit  

2. **`File`**  
   Implémente une file pour effectuer un parcours en largeur.

### **Fonctions Principales**
1. **`minimum(T)`**  
   Trouve le nœud avec la plus petite valeur dans un arbre.

2. **`suppression(T, h)`**  
   Supprime un nœud avec la valeur spécifiée dans l'arbre binaire de recherche (h).

3. **`parcoursLargeur(T)`**  
   Affiche l'arbre niveau par niveau à l'aide d'un parcours en largeur.

---

## **Prérequis**

### Langage
- Python 3.x

### Modules
Aucun module externe requis.

---

## **Installation**
1. Clonez le dépôt ou copiez les fichiers nécessaires.
2. Assurez-vous que Python 3.x est installé sur votre machine.
3. Exécutez le fichier principal pour tester le projet.

---

## **Utilisation**

### Exemple de création d'arbre
```python
# Création de l'arbre
t = Arbre(15)
t.setFilsDroit(18)
t.setFilsGauche(6)

t.getFilsGauche().setFilsGauche(3)
t.getFilsDroit().setFilsDroit(20)

t.getFilsGauche().setFilsDroit(7)
t.getFilsDroit().setFilsGauche(17)

# Affichage initial
print("Arbre initial (parcours en largeur) :", parcoursLargeur(t))
```

### Suppression d'un nœud
```python
# Suppression du nœud avec la valeur 20
suppression(t, 20)

# Affichage après suppression
print("Arbre après suppression de 20 :", parcoursLargeur(t))
```

---

## **Exemple d'Exécution**

### **Avant Suppression :**
```
[15, 6, 18, 3, 7, 17, 20]
```

### **Après Suppression (20 supprimé) :**
```
[15, 6, 18, 3, 7, 17]
```

---

## **Auteurs**
- **Balqis** : Gestion de la logique de suppression et des parcours.  
- **Adil** : Gestion de l'arbre, implémentation des fonctions pour que tout fonctionne.  

---

## **License**
Ce projet est sous licence MIT. Vous pouvez le modifier et l'utiliser librement à des fins éducatives ou personnelles.


