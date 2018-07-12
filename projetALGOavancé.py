import csv
import os

#---------------------DEBUT DE CLASSE---------------------#
class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.filsDroit = None
        self.filsGauche = None

    def ajouterFilsD(self, Noeud):
        self.filsDroit = Noeud

    def ajouterFilsG(self, Noeud):
        self.filsGauche = Noeud

    def supprimerFilsD(self):
        self.filsDroit = None

    def supprimerFilsG(self):
        self.filsGauche = None

    def insert(self, Noeud):
        if self.valeur:
            if(Noeud.valeur < self.valeur):
                if(self.filsGauche == None):
                    self.ajouterFilsG(Noeud)
                else:
                    self.filsGauche.insert(Noeud)

            elif(Noeud.valeur > self.valeur):
                if(self.filsDroit == None):
                    self.ajouterFilsD(Noeud)
                else:
                    self.filsDroit.insert(Noeud)
        else:
            self.valeur = Noeud.valeur

    # Affiche l'arbre en parcours Infixe
    def afficherInfixe(self):
        if self.filsGauche:
            self.filsGauche.afficherInfixe()
        print(self.valeur,";", end='')
        if self.filsDroit:
            self.filsDroit.afficherInfixe()

    # Affiche l'arbre en parcours Postfixe
    def afficherPostfixe(self):
        if self.filsGauche:
            self.filsGauche.afficherPostfixe()
        if self.filsDroit:
            self.filsDroit.afficherPostfixe()
        print(self.valeur,";", end='')

# Supprime le noeud d'un arbre
def deleteNode(root, key):
 
    # Si le noeud courant est la racine
    if root is None:
        return root 
 
    # Si le noeud à supprimer est plus petit que la racine, on va dans le sous-arbre gauche
    if key < root.valeur:
        root.filsGauche = deleteNode(root.filsGauche, key)
 
    # Si le noeud à supprimer est plus petit que la racine, on va dans le sous-arbre droit
    elif(key > root.valeur):
        root.filsDroit = deleteNode(root.filsDroit, key)
 
    # Si le noeud est le même que le noeud principal, alors c'est le noeud à supprimer
    else:
         
        # Noeud avec un seul enfant ou aucun enfant
        if root.filsGauche is None :
            temp = root.filsDroit 
            root = None
            return temp 
             
        elif root.filsDroit is None :
            temp = root.filsGauche 
            root = None
            return temp
 
        # Noeud avec deux enfants: on prend le plus petit dans le sous-arbre droit
        temp = minValueNode(root.filsDroit)
 
        # Copier le successeur infixe du noeud
        root.valeur = temp.valeur
 
        # Supprimer le successeur infixe
        root.filsDroit = deleteNode(root.filsDroit , temp.valeur)
 
 
    return root

## Fonction pour convertir l'INPUT (= une liste representant les noeuds) en un ABR équilibré
def TriListeABR(arr):
     
    if not arr:
        return None
 
    # Pour trouver le noeud du milieu dans la liste
    mid = (len(arr)) // 2
     
    # Prendre le noeud du milieu en tant que racine
    root = Noeud(arr[mid])
     
    # Sous arbre gauche de la racine par selon les valeurs
    root.filsGauche = TriListeABR(arr[:mid])
     
    # Sous arbre droit de la racine par selon les valeurs
    root.filsDroit = TriListeABR(arr[mid+1:])
    return root

## Permet d'afficher larbre apres Tri 
def AffichageABRTri(Noeud):
	if not Noeud:
		return	
	print (Noeud.valeur),
	AffichageABRTri(Noeud.filsGauche)
	AffichageABRTri(Noeud.filsDroit)
	
#---------------------FIN DE CLASSE---------------------#

## Ecrit l'arbre dans un fichier csv ('test.csv', delimiter = ';'),
# le fichier doit être vide au préalable, utiliser "ClearFile()" pour ça.        
# Il faut aussi supprimer le dernier ';', utiliser "DeleteLastChar()" pour ça. 
def ecrireArbreFichier(Noeud):
    myfile = open("test.csv", "a")
    myfile.write(str(Noeud.valeur) + ";")
    myfile.close()
    if Noeud.filsGauche:
        ecrireArbreFichier(Noeud.filsGauche)
    if Noeud.filsDroit:
        ecrireArbreFichier(Noeud.filsDroit)
        
## Importe un arbre depuis un fichier csv ('test.csv', delimiter = ';'),
def LireArbreFichier():
        listeNoeud = FirstCSVRowTOList()
        unNoeud = Noeud(0)
        i = 0
        for i in listeNoeud:
            if unNoeud.valeur == 0:
                unNoeud.valeur = int(i)
            else:
                tempNoeud = Noeud(0)
                tempNoeud.valeur = int(i)
                unNoeud.insert(tempNoeud)
        return unNoeud

## Retourne la premiere ligne(=row) du fichier 'test.csv' sous forme de liste
def FirstCSVRowTOList():
    with open('test.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            return row

## Supprime le dernier caractère d'un fichier        
def DeleteLastChar():
    with open("test.csv", "r") as f:
        file_str = str(f.read())
        file_str = file_str[:-1]
    f.close()
    with open("test.csv", "w") as f:
        f.write(file_str)
    f.close()

## Vide le contenu d'un fichier
def ClearFile():
    open("test.csv", 'w').close()

## Retourne la taille de l'arbre
def tailleArbre(Noeud):
    if Noeud is None:
        return 0
    else:
        return (tailleArbre(Noeud.filsGauche)+ 1 + tailleArbre(Noeud.filsDroit))
      

## Calcule la profondeur MAX "maxProfondeur" d'un arbre sleon le nombre de noeuds -
#Le chemin le plus long depuis le noeud racine jusqu'au noeud le plus éloigné

def maxProfondeur(self):
    if self is None:
        return 0 ; 
 
    else :
 
        # Calcul la profondeur de chaque sous arbre
        GProfondeur = maxProfondeur(self.filsGauche)
        DProfondeur = maxProfondeur(self.filsDroit)
 
        # Prendre la plus grande largeur
        if (GProfondeur > DProfondeur):
            return GProfondeur+1
        else:
            return DProfondeur+1
 

## Permet de rechercher un NOEUD ##
def search(Noeud,key):

    if(Noeud is None):
        return -1
    # Si la racine est NULL ou si cest ma recherche
    elif Noeud.valeur == key:
        return 1
 
    # Ma recherche est plus grand que la valeur du noeudcourant
    elif Noeud.valeur < key:
        return search(Noeud.filsGauche,key)
   
    # Ma recherche est plus petit que la valeur du noeudcourant
    else:
        return search(Noeud.filsDroit,key)


##################
    
monNoeud = Noeud(25) #Déclaration d'un premier Noeud

monNoeud.insert(Noeud(58)) #Insertion d'un Noeud
monNoeud.insert(Noeud(5)) 
monNoeud.insert(Noeud(4))
monNoeud.insert(Noeud(15))
monNoeud.insert(Noeud(3))
monNoeud.insert(Noeud(2))
monNoeud.insert(Noeud(1))

print("Affichage parcours infixe: ")
monNoeud.afficherInfixe()
print("\n")
print("Affichage parcours postefixe: ")
monNoeud.afficherPostfixe()
print("\n")
print("Export de l'arbre vers test.csv")
ClearFile()
ecrireArbreFichier(monNoeud)
DeleteLastChar()
print("Import de l'arbre depuis test.csv")
unNoeud = LireArbreFichier()
print("\n")
print("Affichage parcours infixe du Noeud importé: ")
unNoeud.afficherInfixe()
print("\n")
print("Affichage parcours postfixe du Noeud importé: ")
unNoeud.afficherPostfixe()
print("\n")

print ("La taille de larbre est de %d" %(tailleArbre(monNoeud)))
print ("La hauteur de larbre est %d" %(maxProfondeur(monNoeud)))
print (search(monNoeud,23))

print("Affichage parcours postfixe apres suppresion de 15: ")
unNoeud = deleteNode(unNoeud, 15)
unNoeud.afficherPostfixe()
print("\n")

print ("On saisi les noeuds suivants: 1, 2, 3, 4, 5, 6")
arr = [1, 2, 3, 4, 5, 6]
root = TriListeABR(arr)
print ("ABR triée:")
AffichageABRTri(root)
