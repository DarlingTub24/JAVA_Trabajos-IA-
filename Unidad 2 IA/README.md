Descripcion General:
Este proyecto implementa un sistema de recomendación de películas utilizando Python y Tkinter para la interfaz gráfica, permite a los usuarios iniciar sesion, ver las películas que han visto y recibir recomendaciones basadas en sus preferencias de géneros y actores, además, simula la visualización de nuevas películas y actualiza automáticamente las recomendaciones. La persiste con la información de los usuarios se logra sobreescribiendo el archivo: "data/u.user" con las id de las peliculas vistas por el usuario mientras uso el Sistema de Recomendacion. Ejemplo: si el usuario habia visto antes de usar el sistema la pelicula id=4 (The Matrix) y al usar el sistema ve tambien la pelicula id=1 (Toy Story) en el archivo apareceran las id 4,1.

Estructura del proyecto:

app.py                  
actores.py              
generos.py              
peliculas.py            
usuario.py              
creaciones.py          
GUI_login.py            
GUI_recomendaciones.py  
GUI_verPeliculas.py     
data/                   
  u.actores
  u.genre
  u.pelicula
  u.user

Modulos y Clases:

(Interfaz grafica con Tkinter)

app.py.- Archivo principal que inicializa el sistema, se encarga de cargar todos los datos, iniciarlizar la lista de peliculas y usuarios y iniciar la interfaz login

GUI_login.py.-Muestra la ventana donde el usuario selecciona su perfil para acceder al sistema de recomendaciones, desde aqui se controla el paso a las demas interfaces del programa.

GUI_recomendaciones.py.- Presenta los datos del usuario, las peliculas vistas y las recomendaciones basadas en sus generos y actores preferidos, también permite cambiar de usuario o acceder a la interfaz para ver nuevas peliculas.

GUI_verPeliculas.py.- Permite simular que el usuario ve una nueva pelicula seleccionándola desde un combo box, al hacerlo se actualizan sus preferencias y recomendaciones.

(Clases)

usuario.py.- Define la clase usuario y contiene toda la logica de actualización de peliculas vistas, preferencias, recomendaciones y persistencia de datos.

peliculas.py.- Define la clase peliculas, que representa cada pelicula con su nombre, lista de géneros y lista de actores.

generos.py.- Define la clase generos, usada para identificar los distintos generos disponibles.

actores.py.- Define la clase actores, usada para identificar los distintos actores disponibles.

(Usada para cargar datos por app.py)

creaciones.py.- Genera las listas iniciales de actores, géneros, peliculas y usuarios a partir de los archivos en la carpeta data.


Flujo del Sistema:

1.- Inicio (app.py)

  Carga datos y abre la ventana de login (GUI_login).
  
2.- Login

  Se selecciona de usuario del comboBox, se da click en el boton "Iniciar sesion" y luego se abre la interfaz de recomendaciones.
  
3.- Recomendaciones (GUI_recomendaciones)

  Muestra datos del usuario, peliculas vistas y recomendaciones en base a genero y actores preferidos.
  
  Si se da click en el boton "cambiar de usuario" se vuelve a la interfaz de login (GUI_login).
  
  Si se da click en el boton "Ver Película Nueva" se abre la interfaz que simula ver una pelicula (GUI_verPeliculas).
  
4.- Ver Película Nueva (GUI_verPeliculas)

  Se selecciona una película no vista del comboBox.
  
  Se da click en el boton "VER PELICULA" y se actualiza la lista de peliculas vistas del usuario y las recomendaciones.
  
  Luego se regresa a la interfaz de recomendaciones (GUI_recomendaciones).
  
5.- Persistencia

  Cuando un usuario ve una película nueva (proceso del paso 4), se actualiza data/u.user con la ID de la película vista.
  
  
