from eleve import *
class courso:
    def __init__(self, nom, nombre, descripcion):
        self.nom = nom
        self.nombre = nombre
        self.descripcion = descripcion


    def __str__(self):
        return f'{self.nom} {self.nombre} {self.descripcion}'
