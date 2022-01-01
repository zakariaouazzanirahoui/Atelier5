
#classe Point avec parametre x et y 
class Point:
        def __init__(self, x=0.0, y=0.0):
                self.px = float(x)
                self.py = float(y)
class Segment:
      
        def __init__(self, x1, y1, x2, y2):
#deux parametres pour l'origine 
                self.orig = Point(x1, y1)
#deux parametres pour l'extreme 
                self.extrem = Point(x2, y2)
#methode d'affichage
        def __str__(self):
                return ("Segment : [({0}, {1}), ({2}, {3})]"
                .format(self.orig.px, self.orig.py, self.extrem.px, self.extrem.py))
#fonction main 
if __name__ == '__main__':
        s = Segment(1, 2, 3, 4)
        print(s)
