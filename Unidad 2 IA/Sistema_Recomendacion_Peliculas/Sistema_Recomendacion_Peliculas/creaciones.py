import actores
import generos
import peliculas
import usuario
lista_actores=[]
lista_generos=[]
lista_peliculas=[]
lista_usuarios=[]
def crear_actores(archivo="data/u.actores"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            partes = linea.split("|")
            id_actor=int(partes[0])
            nombre_actor=partes[1]
            actor=actores(id_actor,nombre_actor)
            lista_actores.append(actor)

def crear_generos(archivo="data/u.genre"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            partes = linea.split("|")
            id_genero=int(partes[1])
            nombre_genero=partes[0]
            genero=generos(id_genero,nombre_genero)
            lista_generos.append(genero)

def crear_peliculas(archivo="data/u.pelicula"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            if not linea:
                continue
            generos_pelicula=[]
            actores_pelicula=[]
            partes = linea.split("|")
            id_pelicula=int(partes[0])
            nombre_pelicula=partes[1]
            lista_genres= (int(i) for i in partes[2].split(","))
            lista_acts= (int(i) for i in partes[3].split(","))
            for genero in lista_generos:
               if genero.id in lista_genres:
                   generos_pelicula.append(genero)
            for actor in lista_actores:
               if actor.id in lista_acts:
                   actores_pelicula.append(actor) 
            pelicula=peliculas(id_pelicula,nombre_pelicula,generos_pelicula,actores_pelicula)
            lista_peliculas.append(pelicula)

def crear_usuarios(archivo="data/u.user"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            peliculas_vistas=[]
            if not linea:
                continue
            partes = linea.split("|")
            id_usuario=partes[0]
            nombre_usuario=partes[1]
            lista_vistas= (int(i) for i in partes[2].split(","))
            for pelicula in lista_peliculas:
                if pelicula.id in lista_vistas:
                    peliculas_vistas.append(pelicula)
            usuario_temp=usuario(id_usuario,nombre_usuario,peliculas_vistas)
            if usuario_temp.peliculas_vistas:
                usuario_temp.actualiza_generos()
                usuario_temp.actualiza_actores()
                usuario_temp.actualiza_recomendaciones_generos(lista_peliculas)
                usuario_temp.actualiza_recomendaciones_actores(lista_peliculas)
            lista_usuarios.append(usuario_temp)

