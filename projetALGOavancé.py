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

    def afficherInfixe(self):
        if self.filsGauche:
            self.filsGauche.afficherInfixe()
        print(self.valeur,";", end='')
        if self.filsDroit:
            self.filsDroit.afficherInfixe()

    def ecrireArbreFichier(self):
        myfile = open("test.csv", "a")
        myfile.write(str(self.valeur) + ";")
        
        if self.filsGauche:
            self.filsGauche.ecrireArbreFichier()
        if self.filsDroit:
            self.filsDroit.ecrireArbreFichier()
        myfile.close()

    def LireArbreFichier(self):
        with open('test.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                print(row)
        csvfile.close()
        #supression du derniere caractere:
        #with open("test.csv", 'rb+') as filehandle:
            #filehandle.seek(-1, os.SEEK_END)
            #filehandle.truncate()
        #filehandle.close()

#---------------------FIN DE CLASSE---------------------#
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

     
        


monNoeud = Noeud(25)
monNoeud.insert(Noeud(58))
monNoeud.insert(Noeud(5))
monNoeud.insert(Noeud(4))
monNoeud.insert(Noeud(15))
monNoeud.insert(Noeud(3))
monNoeud.insert(Noeud(2))
monNoeud.insert(Noeud(1))

monNoeud.afficherInfixe()
#monNoeud.ecrireArbreFichier()
#monNoeud.LireArbreFichier()

print ("La taille de larbre est de %d" %(tailleArbre(monNoeud)))
print ("La hauteur de larbre est %d" %(maxProfondeur(monNoeud)))
print (search(monNoeud,15))   
