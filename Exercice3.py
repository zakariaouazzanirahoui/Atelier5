
class Rectangle:
        def __init__(self, longueur=30, largeur=15):
                
                self.lon = longueur
                self.lar = largeur
                self.nom = "rectangle"
#fonction qui calcul la surface
        def surface(self):  
                return self.lon*self.lar
#fonction affichage du Rectangle
        def __str__(self):   
                return ("\nLe {0} de côtes {1} et {2} a une surface de {3}"
                                .format(self.nom, self.lon, self.lar, self.surface()))
class Carre(Rectangle):
       
#constructeur de la class carre
        def __init__(self, cote=10):
                Rectangle.__init__(self, cote, cote)
                self.nom = "carre" # surchage d'attribut d'instance
#fonction main 
if __name__ == '__main__':
        r = Rectangle(12, 8)
        print(r)
        c = Carre()
        print(c)
