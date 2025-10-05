##Constructor de objetos usuario y los metodos para la logica detras de las recomendaciones
class usuario:
    def __init__(self,id,nombre,peliculas=None):
        self.id=id
        self.nombre=nombre
        self.pelis_vistas=peliculas if peliculas else []
        self.generos_preferidos=[]
        self.actores_preferidos=[]
        self.recomendaciones_genero=[]
        self.recomendaciones_actor=[]
    ##Este metodo se encarga de comprobar que la pelicula que va a ver el usuario no sea una ya vista
    ##tambien al comprobar eso actualiza la lista de generos y actores preferidos del usuario y
    ##la lista de recomendaciones en base a esas preferencias.
    def ver_pelicula(self,pelicula,lista_peliculas):
        if pelicula not in self.pelis_vistas:
            self.pelis_vistas.append(pelicula)
            self.actualiza_generos()
            self.actualiza_actores()
            self.actualiza_recomendaciones_generos(lista_peliculas)
            self.actualiza_recomendaciones_actores(lista_peliculas)        
    ##Se encarga de actualizar la lista de generos preferidos del usuario en caso de que
    ##haya un nuevo genero que aniadir, comprueba que no sea uno repetido.
    def actualiza_generos(self):
        for pelis in self.pelis_vistas:
            for genero in pelis.generos:
                if genero not in self.generos_preferidos:
                    self.generos_preferidos.append(genero)
   ##Se encarga de actualizar la lista de actores preferidos del usuario en caso de que
    ##haya un nuevo actor que aniadir, comprueba que no sea uno repetido.
    def actualiza_actores(self):
        for pelis in self.pelis_vistas:
            for actor in pelis.actores:
                if actor not in self.actores_preferidos:
                    self.actores_preferidos.append(actor)
    ##Se encarga de en base a la lista de generos preferidos del usuario generar
    ##una lista de peliculas las cuales no haya visto y que tengan coincidencia
    ##con los generos de su agrado para recomendarselas  
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
    ##Se encarga de en base a la lista de actores preferidos del usuario generar
    ##una lista de peliculas las cuales no haya visto y que tengan coincidencia
    ##con los actores de su agrado para recomendarselas    
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
    ##basicamente el toString de JAVA pero en Python para definir como imprimir los usuarios
    def __str__(self):
        return f"{self.nombre}"

    