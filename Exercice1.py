class Vecteur2D():
   
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y


# initialisation du vecteur v1 sans parametre 
v1 = Vecteur2D()
# initialisation du vecteur v2 avec parametre 
v2 = Vecteur2D(23,-6)

# affichage des deux vecteurs
print("coordonnées de v2: ","(",v2.x,",",v2.y,")")
print("coordonnées de v1: ","(",v1.x,",",v1.y,")")
