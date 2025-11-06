# Importa la libreria Tkinter para crear la ventana
import tkinter as tk

#Importa el modulo (archivo .py) que contiene la clase de la interfaz
import Interfaz

#Esto asegura que el codigo se ejecute cuando se ejecuta este archivo 
if __name__ == "__main__":
    
    #Crea la ventana principal de la aplicacion
    ventana=tk.Tk()
    
    #Crea una instancia de la clase LoginInterfaz  y le pasa la ventana principal
    app = Interfaz.LoginInterfaz(ventana)

    #Inicia el bucle principal de la aplicacion para que la ventana se mantenga abierta, esperando la interaccion del usuarrio hasta que se cierre
    ventana.mainloop()
