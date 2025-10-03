class usuario:
    def __init__(self,id,nombre,peliculas):
        self.id=id
        self.nombre=nombre
        self.pelis_vistas=[peliculas]
        self.generos_preferidos=[]
        self.actores_preferidos=[]
        self.recomendaciones_genero=[]
        self.recomendaciones_actor=[]

    def ver_pelicula(self,pelicula,lista_peliculas):
        if pelicula not in self.pelis_vistas:
            self.pelis_vistas.append(pelicula)
            self.actualiza_generos()
            self.actualiza_actores()
            self.actualiza_recomendaciones_generos(lista_peliculas)
            self.actualiza_recomendaciones_actores(lista_peliculas)        
    
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

    def actualiza_recomendaciones_generos(self,lista_peliculas):
        rankeo_peliculasXgeneros=[]
        coincidencias=0
        for pelicula in lista_peliculas:
            if pelicula not in self.pelis_vistas:
                for genero in pelicula.generos:
                    if genero in self.generos_preferidos:
                        coincidencias+=1
                if coincidencias>0:
                    rankeo_peliculasXgeneros.append((pelicula,coincidencias))
                    coincidencias=0
        rankeo_peliculasXgeneros.sort(key=lambda x: x[1],reverse=True)
        self.recomendaciones_genero=[peli[0] for peli in rankeo_peliculasXgeneros]
        
    def actualiza_recomendaciones_actores(self,lista_peliculas):
        rankeo_peliculasXactores=[]
        coincidencias=0
        for pelicula in lista_peliculas:
            if pelicula not in self.pelis_vistas:
                for actor in pelicula.actores:
                    if actor in self.actores_preferidos:
                        coincidencias+=1
                if coincidencias>0:
                    rankeo_peliculasXactores.append((pelicula,coincidencias))
                    coincidencias=0
        rankeo_peliculasXactores.sort(key=lambda x: x[1],reverse=True)
        self.recomendaciones_actor=[peli[0] for peli in rankeo_peliculasXactores]

    