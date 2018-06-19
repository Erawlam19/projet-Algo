
# Print the tree
    def PrintTree(self):
        if self.filsgauche:
            self.fislgauche.PrintTree()
        print( self.valeur),
        if self.filsDroit:
            self.filsDroit.PrintTree()
			

monNoeud = noeud(3)
monNoeud.ajouter(2)
monNoeud.ajouter(34)

monNoeud.PrintTree()