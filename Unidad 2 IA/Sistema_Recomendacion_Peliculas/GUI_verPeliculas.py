import tkinter as tk
from tkinter import ttk
##Interfaz
##Esta interfaz sirve para simular que el usuario ve una pelicula nueva
##una vez selecciona una del comboBox y da click en el boton "VER PELICULA"
##es regresado a la anterior interfaz (la de recomendaciones).
class VerPeliculasInterfaz:
    def __init__(self,ventana,usuario,lista_peliculas,ventana_padre,instancia):
        self.ventana=ventana
        self.ventana.title("Ver Peliculas")
        width = 400
        height = 400
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.rowconfigure(4,weight=1)        
        self.ventana_padre=ventana_padre
        self.instancia_ventanaPadre=instancia
        self.texto= tk.Label(self.ventana,text="Seleccione una Pelicula a ver:")
        self.texto.grid(row=1,column=0,padx=0,pady=10,sticky="nsew")
        self.ventana.columnconfigure(0,weight=1)
        ##Crear ComboBox
        lista=[str(peli.nombre) for peli in lista_peliculas if peli not in usuario.pelis_vistas]
        self.comboBox= ttk.Combobox(self.ventana, values=lista,state="readonly")
        self.comboBox.grid(row=2,column=0,padx=10,pady=10,sticky="nsew")
        boton= tk.Button(self.ventana,text="VER PELICULA",command=lambda: self.cambio_interfaz(usuario,lista_peliculas))
        boton.grid(row=3,column=0,padx=10,pady=10,sticky="nsew")
        self.ventana.protocol("WM_DELETE_WINDOW", self.devolver_recom)
    ##Este metodo sirve para cuando se cierra la ventana con la "X" de la esquina derecha de arriba
    def devolver_recom(self):
        self.ventana.destroy()
        self.ventana_padre.deiconify()
    ##Este metodo sirve para que una vez el usuario selecciono una pelicula para ver
    ## se le devuelva a la interfaz anterior y ademas se actualizen las cosas en esa interfaz
    def cambio_interfaz(self,usuario,lista_peliculas):
        pelicula=self.comboBox.get()
        if not pelicula:
            return
        pelicula_obj=next((objeto for objeto in lista_peliculas if objeto.nombre==pelicula),None)
        usuario.ver_pelicula(pelicula_obj,lista_peliculas)
        self.instancia_ventanaPadre.actualizar_interfaz(usuario,lista_peliculas)
        self.ventana.destroy()
        self.ventana_padre.deiconify()
        