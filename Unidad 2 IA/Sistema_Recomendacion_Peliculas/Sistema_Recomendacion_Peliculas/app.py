import pandas as pd

# Cargar ratings
ratings = pd.read_csv("data/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])
# Cargar películas
movies = pd.read_csv("data/u.item", sep="|", encoding="latin-1", 
                     names=["item_id", "title", "release_date", "video_release_date", "IMDb_URL",
                            "unknown","Action","Adventure","Animation","Children","Comedy","Crime",
                            "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery",
                            "Romance","Sci-Fi","Thriller","War","Western"])



# def recabaGeneros(fila,movies_general):
#     lista_generos=set()
#     fila_pelicula=movies_general[movies_general["item_id"]==fila["item_id"]].iloc[0]
#     generos=["unknown","Action","Adventure","Animation","Children","Comedy","Crime",
#             "Documentary","Drama","Fantasy","Film-Noir","Horror","Musical","Mystery",
#             "Romance","Sci-Fi","Thriller","War","Western"]
#     for genero in generos:
#         if fila_pelicula[genero]==1:
#             lista_generos.add(genero)
#     return lista_generos


# def peliculasRecomendadas(lista_generos,rating_usuario,movies_general):
#     rankeo_peliculas=[]
#     coincidencias=0
#     #Aqui se recorre toda la lista de peliculas y se comprueba cuales de los
#     #generos de las peliculas que no ha visto el usuario estan en la lista
#     #y 
#     for i in range(len(movies_general)):
#         fila_pelicula=movies_general.iloc[i]
#         if fila_pelicula["item_id"]not in rating_usuario["item_id"].values:
#             generos_temporal=recabaGeneros(fila_pelicula,movies_general)
#             coincidencias=len(generos_temporal & lista_generos)
#             if coincidencias>0:
#                 rankeo_peliculas.append([fila_pelicula,coincidencias])
#     rankeo_peliculas.sort(key=lambda x: x[1],reverse=True)
#     return rankeo_peliculas
            


# def recomendaciones( id_usuario,rating, movie):
#     rating_general=rating
#     rating_usuario = rating_general[rating_general["user_id"]==id_usuario]
#     movies_general=movie
#     lista_generos=set()
#     #En este for se almacena en un set() llamado lista_generos todos los generos que le gustan
#     #en base a las peliculas que haya raiteado con 3 o mas estrellas
#     for i in range(len(rating_usuario)):
#         fila=rating_usuario.iloc[i]
#         if fila["rating"]>=3 :
#             lista_generos|=recabaGeneros(fila,movies_general)
#     return peliculasRecomendadas(lista_generos,rating_usuario,movies_general)