from eleve import *
class courso:
    def __init__(self, nom, nombre, descripcion,attribut_de_git, courriel, sigle_cours):
        self.nom = nom
        self.nombre = nombre
        self.descripcion = descripcion
        self.attribut_de_git = attribut_de_git
        self.courriel = courriel
        self.sigle_cours = sigle_cours

    def __str__(self):
        return f'{self.nom} {self.nombre} {self.sigle_cours}'
    

i=1
for i in 10:
    i += 1
    #ddddddddddddddddddddddddddddddddddddddddddddddddddd
