from eleve import *
class courso:
    def __init__(self, nom, nombre, descripcion,attribut_de_git):
        self.nom = nom
        self.nombre = nombre
        self.descripcion = descripcion
        self.attribut_de_git = attribut_de_git

    def __str__(self):
        return f'{self.nom} {self.nombre} {self.descripcion}'
