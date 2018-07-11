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

    #Affiche l'arbre en parcours Infixe
    def afficherInfixe(self):
        if self.filsGauche:
            self.filsGauche.afficherInfixe()
        print(self.valeur,";", end='')
        if self.filsDroit:
            self.filsDroit.afficherInfixe()

    #Affiche l'arbre en parcours Postfixe
    def afficherPostfixe(self):
        if self.filsGauche:
            self.filsGauche.afficherPostfixe()
        if self.filsDroit:
            self.filsDroit.afficherPostfixe()
        print(self.valeur,";", end='')


#---------------------FIN DE CLASSE---------------------#

#Ecrit l'arbre dans un fichier csv ('test.csv', delimiter = ';'),
#le fichier doit être vide au préalable, utiliser "ClearFile()" pour ça.        
#Il faut aussi supprimer le dernier ';', utiliser "DeleteLastChar()" pour ça. 
def ecrireArbreFichier(Noeud):
    myfile = open("test.csv", "a")
    myfile.write(str(Noeud.valeur) + ";")
    myfile.close()
    if Noeud.filsGauche:
        ecrireArbreFichier(Noeud.filsGauche)
    if Noeud.filsDroit:
        ecrireArbreFichier(Noeud.filsDroit)
        
#Importe un arbre depuis un fichier csv ('test.csv', delimiter = ';'),
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

#Retourne la premiere ligne(=row) du fichier 'test.csv' sous forme de liste
def FirstCSVRowTOList():
    with open('test.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            return row

#Supprime le dernier caractère d'un fichier        
def DeleteLastChar():
    with open("test.csv", "r") as f:
        file_str = str(f.read())
        file_str = file_str[:-1]
    f.close()
    with open("test.csv", "w") as f:
        f.write(file_str)
    f.close()

#Vide le contenu d'un fichier
def ClearFile():
    open("test.csv", 'w').close()

#retourne la taille de l'arbre
def tailleArbre(Noeud):
    if Noeud is None:
        return 0
    else:
        return (tailleArbre(Noeud.filsGauche)+ 1 + tailleArbre(Noeud.filsDroit))
      

#Calcule la profondeur MAX "maxProfondeur" d'un arbre sleon le nombre de noeuds -
#Le chemin le plus long depuis le noeud racine jusqu'au noeud le plus éloigné

def maxProfondeur(self):
    if self is None:
        return 0 ; 
 
    else :
 
        # Compute the Profondeur of each subtree
        GProfondeur = maxProfondeur(self.filsGauche)
        DProfondeur = maxProfondeur(self.filsDroit)
 
        # Use the larger one
        if (GProfondeur > DProfondeur):
            return GProfondeur+1
        else:
            return DProfondeur+1
 

#Penser à rajouter un return, si la valeur n'est pas trouvée
def search(self,key):
     
    # Si la racine est NULL ou si cest ma recherche
    if self.valeur == key:
        return 1
 
    # Ma recherche est plus grand que la valeur du noeudcourant
    if self.valeur < key:
        return search(self.filsDroit,key)
   
    # Ma recherche est plus petit que la valeur du noeudcourant
    return search(self.filsGauche,key)



    
monNoeud = Noeud(25) #Déclaration d'un premier Noeud

monNoeud.insert(Noeud(58)) #Insertion d'un Noeud
monNoeud.insert(Noeud(5)) 
monNoeud.insert(Noeud(4))
monNoeud.insert(Noeud(15))
monNoeud.insert(Noeud(3))
monNoeud.insert(Noeud(2))
monNoeud.insert(Noeud(1))

print("Affichage infixe: ")
monNoeud.afficherInfixe()
print("\n")
print("Affichage postefixe: ")
monNoeud.afficherPostfixe()
print("\n")
print("Export de l'arbre vers test.csv")
ClearFile()
ecrireArbreFichier(monNoeud)
DeleteLastChar()
print("Import de l'arbre depuis test.csv")
unNoeud = LireArbreFichier()
print("Affichage infixe du Noeud importé: ")
unNoeud.afficherInfixe()
print("Affichage postfixe du Noeud importé: ")
unNoeud.afficherPostfixe()



#print ("La taille de larbre est de %d" %(tailleArbre(monNoeud)))
#print ("La hauteur de larbre est %d" %(maxProfondeur(monNoeud)))
#print (search(monNoeud,15))   
