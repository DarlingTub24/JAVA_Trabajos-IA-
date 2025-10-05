##Cpnstructor de objetos peliculas
class peliculas:
    def __init__(self,id,nombre,generos,actores):
        self.id=id
        self.nombre=nombre
        self.generos=generos
        self.actores=actores
    
    def __str__(self):
        str_generos=[str(genero) for genero in self.generos]
        str_actores=[str(actor) for actor in self.actores]
        return f"{self.nombre}, Generos: {str_generos}, Actores: {str_actores}"