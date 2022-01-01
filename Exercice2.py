class Vecteur2D():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def Display(self):
        print('coordonnées de ce vecteur: ({0},{1})'.format(self.x,self.y))

    def __add__(self,other):
        result = Vecteur2D(self.x+other.x,self.y+other.y)
        return result


# initialisation des deux vecteurs
v1 = Vecteur2D(12,34)
v2 = Vecteur2D(23,-6)

# affichage des deux vecteurs
v1.Display()
v2.Display()

# la somme
som = v1 + v2
print('la somme de v1 et v2 est:')
som.Display()
