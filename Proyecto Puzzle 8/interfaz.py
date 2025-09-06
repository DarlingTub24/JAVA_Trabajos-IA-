#importamos toda la clase puzzle8 que es la que contiene los
#distintos metodos a utilizar en la interfaz grafica
import puzzle8
import tkinter as tk
class PuzzleInterfaz:
    #Constructor de tipo PuzzleInterfaz y a la vez donde se crea lo necesario para
    #mostrar la Matriz inicial, los botones para: "Restablecer" y "Resolver"
    #y tambien para mostrar ya sea el camino de matrices que lleva a la solucion
    #o un texto que indique que dicha Matriz inicial no tiene solucion alguna.
    #Para esto tuve que importar tkinter bajo el nombre de tk, para utilizar por ejemplo:
    #Button, Text, Label y ScrollBar
    def __init__(self,ventana):
        self.ventana=ventana
        self.tablero=puzzle8.restablecer([0,1,2,3,4,5,6,7,8])
        self.tablero_label = tk.Label(self.ventana, text=self.formato_Tablero(self.tablero))
        self.tablero_label.grid(row=0,column=0,padx=10,pady=10)
        boton1= tk.Button(self.ventana,text="Restablecer",command=self.interfaz_restablecer)
        boton1.grid(row=0, column=1, padx=10, pady=10)
        boton2= tk.Button(self.ventana,text="Resolver",command=self.interfaz_resolver)
        boton2.grid(row=1, column=1, padx=10, pady=10)
        self.texto=tk.Text(self.ventana, width=22, height=10)
        self.scrollBar=tk.Scrollbar(self.ventana, command=self.texto.yview)
        self.texto.configure(yscrollcommand=self.scrollBar.set)
        self.texto.grid(row=1, column=0, padx=10, pady=10)
        self.scrollBar.grid(row=1, column=0, sticky="nse",padx=10, pady=10)
        self.texto.config(state=tk.DISABLED)
    #Metodo para hacer uso de restablecer, que es importado del otro archivo py
    def interfaz_restablecer(self):
        self.tablero=puzzle8.restablecer([0,1,2,3,4,5,6,7,8])
        self.tablero_label.config( text=self.formato_Tablero(self.tablero))
    #Metodo para darle formato a las matrices que se impriman, pq sino salian asi: [1,2,3],[4,5,6],[7,8,0]
    def formato_Tablero(self,tablero):
        orden=""
        for filas in tablero:
            orden= orden + str(filas) + "\n"
        return orden
    
    #Metodo para hacer uso de puzzle8 (el metodo que resuelve el juego), que es importado del otro archivo py
    def interfaz_resolver(self):
        camino=puzzle8.puzzle8(self.tablero,puzzle8.solucionFinal)
        #Hace que el texto sea editable aqui en codigo
        self.texto.config(state=tk.NORMAL)
        #Limpiar en caso que haya un camino ya escrito
        self.texto.delete(1.0, tk.END)
        if camino:
            for paso in camino:
                self.texto.insert(tk.END,self.formato_Tablero(paso)+"\n")
            self.texto.config(state=tk.DISABLED)
        else:
            self.texto.insert(tk.END,"Tablero sin Solucion") 
            self.texto.config(state=tk.DISABLED) 
           
#Se crea la ventana de la Interfaz, se le da titulo y tamaño
ventana=tk.Tk()
ventana.title("Puzzle8")
ventana.geometry("300x300")
#Se crea una Instancia de la clase
juegoP8 = PuzzleInterfaz(ventana)
#Se mantiene en Loop la interfaz, porque de no hacerlo se cerraria justo despues de abrirse
ventana.mainloop()