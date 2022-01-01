class Etudiant:
    """defintion du class"""
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne


# la liste d'etudiant
studentsList = [ Etudiant("Ahmed", "Afilad", 20, "P18989898", 17),
             Etudiant("Zakaria", "Ouazzani", 21, "P18989898", 12),
             Etudiant(" Mohammed", "EL Asri", 22, "P18989898", 8),
             Etudiant("Soufian", "Nemouh", 21, "P18989898", 15),
             Etudiant("Moad", "El Ghayati", 23, "P18989898", 11.5)]

# triage selon l'age 
def sortByAge(student):
    return student.age

studentsList.sort(key=sortByAge)

for student in studentsList:
    print("==========")
    print(student.nom)
    print(student.prenom)
    print(student.age)
print("=======end of list=============")

# triage selon la moyenne
def sortByAverage(student):
    return student.moyenne

studentsList.sort(key=sortByAverage)

for student in studentsList:
    print("==========")
    print(student.nom)
    print(student.prenom)
    print(student.moyenne)

print("=======end of list=============")
