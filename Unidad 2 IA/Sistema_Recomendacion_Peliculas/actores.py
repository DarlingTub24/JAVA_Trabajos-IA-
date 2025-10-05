##Constructor de objetos actores
class actores:
    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre
    def __str__(self):
        return f"{self.nombre}"