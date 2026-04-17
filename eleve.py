#class cours
#gg
class Cours:
    def __init__(self, nom, enseignant):
        self.nom = nom
        self.enseignant = enseignant
        self.eleves = []

    def inscrire(self, eleve):
        self.eleves.append(eleve)


    def __str__(self):
        return f'{self.nom} {self.enseignant}'
#class eleve
class Eleve:
    def __init__(self, nom):
        self.nom = nom

    
