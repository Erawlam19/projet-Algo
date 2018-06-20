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
        with open("test.csv", "a") as myfile:
            temp = str(self.valeur) + ";"
            myfile.write(temp)
            if self.filsGauche:
                self.filsGauche.ecrireArbreFichier()
            if self.filsDroit:
                self.filsDroit.ecrireArbreFichier()
        myfile.close()

    def LireArbreFichier(self):
        with open("test.csv", "a") as myfile:
            temp = str(self.valeur) + ";"
            myfile.write(temp)
            if self.filsGauche:
                self.filsGauche.ecrireArbreFichier()
            if self.filsDroit:
                self.filsDroit.ecrireArbreFichier()
        myfile.close()
                    
        
        


monNoeud = Noeud(2)
monNoeud.insert(Noeud(3))
monNoeud.insert(Noeud(5))
monNoeud.insert(Noeud(1))
monNoeud.insert(Noeud(15))
monNoeud.insert(Noeud(0))

monNoeud.afficherInfixe()
print("\n")
monNoeud.ecrireArbreFichier()

