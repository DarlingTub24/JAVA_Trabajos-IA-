import tkinter as tk
from tkinter import ttk
import GUI_recomendaciones

##Interfaz
##Esta Interfaz se encarga de mostrarle al usuario usando el programa
##una lista de usuarios a seleccionar para iniciar sesion, una vez se seleccionar uno
##le debe dar click al boton "Iniciar Sesion" y sera trasladado a la interfaz del
##sistema de recomendacion
class LoginInterfaz:
    def __init__(self,ventana,lista_peliculas,lista_usuarios):
        self.ventana=ventana
        self.ventana.title("Inicio de Sesion")
        self.lista_peliculas=lista_peliculas
        self.lista_usuarios=lista_usuarios
        width = 400
        height = 400
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.rowconfigure(4,weight=1)
        self.texto= tk.Label(self.ventana,text="Seleccione un Usuario:")
        self.texto.grid(row=1,column=0,padx=0,pady=10,sticky="ew")
        self.ventana.columnconfigure(0,weight=1)
        ##Crear ComboBox
        lista=self.lista_usuarios
        self.comboBox= ttk.Combobox(self.ventana, values=lista,state="readonly")
        self.comboBox.grid(row=2,column=0,padx=10,pady=10,sticky="ew")
        boton= tk.Button(self.ventana,text="Iniciar Sesion",command=self.cambio_interfaz)
        boton.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
    ##Metodo hecho para el cambio a la interfaz del Sistema de Recomendacion como se menciono arriba
    def cambio_interfaz(self):
        usuario=self.comboBox.get()
        if not usuario:
            return
        usuario_obj=next((objeto for objeto in self.lista_usuarios if objeto.nombre==usuario),None)
        self.ventana.withdraw()
        ventana_sistema=tk.Toplevel()
        GUI_recomendaciones.RecomendacionesInterfaz(ventana_sistema,usuario_obj,self.lista_peliculas,self.ventana)
