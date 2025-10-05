import tkinter as tk
import GUI_verPeliculas
##Interfaz
##Esta interfaz se encarga de mostrarle al usuario sus datos,
##las peliculas que ha visto (o si no ha visto ninguna) y las recomendaciones
##en base a los generos o a los actores que prefiere, ademas
##se tienen 2 botones, ekl primero "Cambiar usuario" sirve para
##devolverse a la interfaz anterior y seleccionar otro usuario.
##El 2do boton es para simular que se ven peliculas no vistas,
##te traslada a la interfaz de verPeliculas.
class RecomendacionesInterfaz:
    def __init__(self,ventana,usuario,lista_peliculas,ventana_padre):
        self.ventana=ventana
        self.ventana.title("Sistema de Recomendacion")
        width = 800
        height = 800
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")
        self.ventana.rowconfigure(0,weight=1)                
        self.ventana.rowconfigure(10,weight=1)
        self.ventana.columnconfigure(0,weight=1)                
        self.ventana.columnconfigure(3,weight=1)
        self.ventana_padre=ventana_padre
        boton1=tk.Button(self.ventana,text="Cambiar Usuario", command= self.cambiar_usuario)
        boton1.grid(row=1,column=2,padx=0,pady=10,sticky="nsew")
        self.texto1=tk.Label(self.ventana,text="Datos del Usuario:")
        self.texto1.grid(row=1,column=1,padx=0,pady=10,sticky="nsew")
        self.texto2=tk.Label(self.ventana,text=f"ID: {usuario.id}, Nombre: {usuario.nombre}")
        self.texto2.grid(row=2,column=1,padx=0,pady=10,sticky="nsew")
        self.texto3=tk.Label(self.ventana,text="Peliculas Vistas:")
        self.texto3.grid(row=3,column=1,padx=0,pady=10,sticky="nsew")
        pelis="\n".join([str(peli) for peli in usuario.pelis_vistas])
        self.texto4=tk.Label(self.ventana,text=pelis)
        self.texto4.grid(row=4,column=1,padx=0,pady=10,sticky="nsew")
        self.texto5=tk.Label(self.ventana,text="Peliculas recomendadas en base a generos preferidos:")
        self.texto5.grid(row=5,column=1,padx=0,pady=10,sticky="nsew")
        recom_genero="\n".join([str(peli) for peli in usuario.recomendaciones_genero])
        self.texto6=tk.Label(self.ventana,text=recom_genero)
        self.texto6.grid(row=6,column=1,padx=0,pady=10,sticky="nsew")
        self.texto7=tk.Label(self.ventana,text="Peliculas recomendadas en base a actores preferidos:")
        self.texto7.grid(row=7,column=1,padx=0,pady=10,sticky="nsew")
        recom_actor="\n".join([str(peli) for peli in usuario.recomendaciones_actor])
        self.texto8=tk.Label(self.ventana,text=recom_actor)
        self.texto8.grid(row=8,column=1,padx=0,pady=10,sticky="nsew")
        self.boton2=tk.Button(self.ventana,text="Ver Pelicula Nueva", command=lambda: self.ver_pelicula(usuario,lista_peliculas))
        self.boton2.grid(row=9,column=1,padx=0,pady=10,sticky="nsew")
        if len(usuario.pelis_vistas)==len(lista_peliculas):
            self.boton2.config(state="disabled")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_app)
    ##Metodo para cuando se cierra la ventana con la X de la esquina derecha de arriba
    def cerrar_app(self):
        self.ventana.quit()
        self.ventana.destroy()
    ##Metodo para actualizar las peliculas vistas por el usuario y las redomendaciones
    ##cuando se ve una nueva pelicula, este metodo es usado en la interfaz de verPeliculas
    def actualizar_interfaz(self,usuario,lista_peliculas):
        self.texto2.config(text=f"ID: {usuario.id}, Nombre: {usuario.nombre}")
        pelis="\n".join([str(peli) for peli in usuario.pelis_vistas])
        self.texto4.config(text=pelis)
        recom_genero="\n".join([str(peli) for peli in usuario.recomendaciones_genero])
        self.texto6.config(text=recom_genero)
        recom_actor="\n".join([str(peli) for peli in usuario.recomendaciones_actor])
        self.texto8.config(text=recom_actor)
        if len(usuario.pelis_vistas)==len(lista_peliculas):
            self.boton2.config(state="disabled")

    ##MEtodo para devolverse a la interfaz de login se acciona con el boton "Cambiar usuario"
    def cambiar_usuario(self):
        self.ventana.destroy()
        self.ventana_padre.deiconify()
    
    ##Metodo para cambiar a la interfaz de verPeliculas
    def ver_pelicula(self,usuario,lista_peliculas):
        self.ventana.withdraw()
        ventana_verPelis=tk.Toplevel()
        GUI_verPeliculas.VerPeliculasInterfaz(ventana_verPelis,usuario,lista_peliculas,self.ventana,self)




        