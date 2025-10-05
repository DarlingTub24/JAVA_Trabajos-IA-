import tkinter as tk
from tkinter import ttk
import creaciones
import GUI_login
##Se crean los elementos necesarios
creaciones.crear_actores()
creaciones.crear_generos()
creaciones.crear_peliculas()
creaciones.crear_usuarios()

##Se recaban las distintas listas
lista_peliculas=creaciones.lista_peliculas
lista_usuarios=creaciones.lista_usuarios
##Se usa la interfaz del Login que a su vez usa las demas interfaces
##le pasamos las listas con los datos
if __name__ == "__main__":
    ventana=tk.Tk()
    app = GUI_login.LoginInterfaz(ventana,lista_peliculas,lista_usuarios)
    ventana.mainloop()


