class usuario:
    def __init__(self,id,nombre):
        self.id=id
        self.nombre=nombre
        self.pelis_vistas=[]
        self.generos_preferidos=[]
        self.actores_preferidos=[]
        self.recomendaciones=[]

    def ver_pelicula(self,pelicula,lista_peliculas):
        if pelicula not in self.pelis_vistas:
            self.pelis_vistas.append(pelicula)
            self.actualiza_generos()
            self.actualiza_actores()
            self.actualiza_recomendaciones(lista_peliculas)        
    
    def actualiza_generos(self):
        for pelis in self.pelis_vistas:
            for genero in pelis.generos:
                if genero not in self.generos_preferidos:
                    self.generos_preferidos.append(genero)
    def actualiza_actores(self):
        for pelis in self.pelis_vistas:
            for actor in pelis.actores:
                if actor not in self.actores_preferidos:
                    self.actores_preferidos.append(actor)

    def actualiza_recomendaciones(self,lista_peliculas):
        rankeo_peliculas=[]
        coincidencias=0
        for pelicula in lista_peliculas:
            if pelicula not in self.pelis_vistas:
                for genero in pelicula.generos:
                    if genero in self.generos_preferidos:
                        coincidencias+=1
                rankeo_peliculas.append((pelicula,coincidencias))
                coincidencias=0
        rankeo_peliculas.sort(key=lambda x: x[1],reverse=True)
        self.recomendaciones=[peli[0] for peli in rankeo_peliculas]

    