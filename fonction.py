
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

    def insert(self, data):
# Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data