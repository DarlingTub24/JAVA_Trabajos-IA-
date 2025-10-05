import actores
import generos
import peliculas
import usuario
##Se crean las listas que contendran los objetos de tipos:
##usuario,peliculas,generos y actores
lista_actores=[]
lista_generos=[]
lista_peliculas=[]
lista_usuarios=[]
##Este metodo se encarga de recabar de el documento u.actores que se encuentra en la
##carpeta data la informacion de los distintos renglones que contienen la id de cada actor
## y su nombre, entonces crea los objetos actores con esos datos y los almacena en lista_autores
def crear_actores(archivo="data/u.actores"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            partes = linea.strip().split("|")
            id_actor=int(partes[0])
            nombre_actor=partes[1]
            actor=actores.actores(id_actor,nombre_actor)
            lista_actores.append(actor)
##Este metodo se encarga de recabar de el documento u.genre que se encuentra en la
##carpeta data la informacion de los distintos renglones que contienen el nombre y la id de cada genero,
##entonces crea los objetos generos con esos datos y los almacena en lista_generos
def crear_generos(archivo="data/u.genre"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            partes = linea.strip().split("|")
            nombre_genero=partes[0]
            id_genero=int(partes[1])
            genero=generos.generos(id_genero,nombre_genero)
            lista_generos.append(genero)
##Este metodo se encarga de recabar de el documento u.pelicula que se encuentra en la
##carpeta data la informacion de los distintos renglones que contienen la id de cada pelicula
## , su nombre, la id de los generos a los que pertenece y la id de los actores que salen en la pelicula 
##entonces crea los objetos peliculas con esos datos y los almacena en lista_peliculas
def crear_peliculas(archivo="data/u.pelicula"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            generos_pelicula=[]
            actores_pelicula=[]
            partes = linea.strip().split("|")
            id_pelicula=int(partes[0])
            nombre_pelicula=partes[1]
            lista_genres= [int(i) for i in partes[2].split(",")]
            lista_acts= [int(i) for i in partes[3].split(",")]
            for genero in lista_generos:
               if genero.id in lista_genres:
                   generos_pelicula.append(genero)
            for actor in lista_actores:
               if actor.id in lista_acts:
                   actores_pelicula.append(actor) 
            pelicula=peliculas.peliculas(id_pelicula,nombre_pelicula,generos_pelicula,actores_pelicula)
            lista_peliculas.append(pelicula)
##Este metodo se encarga de recabar de el documento u.user que se encuentra en la
##carpeta data la informacion de los distintos renglones que contienen la id de cada usuario
## , su nombre y la id de las peliculasque ha visto, o si no ha visto ninguna igualmente, 
##entonces crea los objetos usuario con esos datos y los almacena en lista_usuarios
def crear_usuarios(archivo="data/u.user"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            peliculas_vistas=[]
            if not linea:
                continue
            partes = linea.strip().split("|")
            id_usuario=partes[0]
            nombre_usuario=partes[1]
            lista_vistas= [int(i) for i in partes[2].split(",") if i.isdigit()]
            if lista_vistas:
                for pelicula in lista_peliculas:
                    if pelicula.id in lista_vistas:
                        peliculas_vistas.append(pelicula)
            usuario_temp=usuario.usuario(id_usuario,nombre_usuario,peliculas_vistas)
            if usuario_temp.pelis_vistas:
                usuario_temp.actualiza_generos()
                usuario_temp.actualiza_actores()
                usuario_temp.actualiza_recomendaciones_generos(lista_peliculas)
                usuario_temp.actualiza_recomendaciones_actores(lista_peliculas)
            lista_usuarios.append(usuario_temp)

