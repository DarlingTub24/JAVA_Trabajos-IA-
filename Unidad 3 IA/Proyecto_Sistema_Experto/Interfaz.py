#Importacion de libreria TINKER para la interfaz
import tkinter as tk
# Importa el modulo (otro archivo .py) que contiene la base de conocimientos (el catalogo de enfermedades)
import Sistema_Experto

# Define la clase principal de la interfaz de diagnostico
class LoginInterfaz:

    # Metodo constructor, se ejecuta al crear una instancia de la clase que recibe la ventana principal.
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Sistema Experto")

        # Definimos las dimensiones de la ventana
        width = 400
        height = 400

        # Calcula las coordenadas X e Y para centrar la ventana en la pantalla
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2

        # Aplica el tamaño y posicion a la ventana
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")

        # Configura las filas 0 y 4 para que se expandan
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.rowconfigure(4,weight=1)
        
        # Carga el catalogo de enfermedades desde el modulo importado
        self.lista_enfermedades=Sistema_Experto.catalogo_Enfermedades
        
        # Inicializa una lista vacia para guardar los sintomas que el paciente si y no tiene
        self.lista_paciente=[]
        self.lista_NOsintomas=[]
        
        # Crea una etiqueta donde se mostraran las preguntas y el resultado
        self.texto= tk.Label(self.ventana,text="",wraplength=350,justify="center")
        
        # Posiciona la etiqueta
        self.texto.grid(row=1,column=0,padx=0,pady=10,sticky="ew")
        
        # Configura la columna 0 para que se expanda, centrando horizontalmente el contenido
        self.ventana.columnconfigure(0,weight=1)
        
        # Crea el boton "Si" y lo vincula al metodo
        self.botonSI= tk.Button(self.ventana,text="Si",command=lambda: self.respuesta("Si"))
        
        # Posiciona el boton Si
        self.botonSI.grid(row=2,column=0,padx=0,pady=10,sticky="ew")
        
        # Crea el boton No
        self.botonNO= tk.Button(self.ventana,text="No",command=lambda: self.respuesta("No"))
        
        # Posiciona el boton No
        self.botonNO.grid(row=3,column=0,padx=0,pady=10,sticky="ew")
        
        # Inicializa un indice para rastrear el sintoma actual que se esta preguntando
        self.posicionSintoma=0
        
        # Inicializa un indice para rastrear la enfermedad actual que se esta evaluando
        self.posicionEnfermedad=0
        
        # Variable temporal usada para buscar la proxima enfermedad
        self.posicionEnfermedadTemporal=0
        self.generacion_pregunta()

    # Metodo encargado de mostrar la siguiente pregunta al usuario
    def generacion_pregunta(self):
        
         # Comprueba si el sintoma actual aun no ha sido preguntado
        if self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma] not in self.lista_NOsintomas and self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma] not in self.lista_paciente:
            
            # Si no se ha preguntado, actualiza el texto de la etiqueta con la pregunta
            self.texto.configure(text="Usted Presenta el Siguiente Sintoma: " + self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
        else:
            
            #Si el sintoma ya se pregunto salta al siguiente sintoma y llama recursivamente a la funcion para encontrar el proximo sintoma valido
            self.posicionSintoma+=1
            self.generacion_pregunta()


    # Metodo que se ejecuta cuando el usuario presiona Si o No      
    def respuesta(self,respuesta):

       
        if respuesta=="Si":

            # Añade el sintoma actual a la lista de sintomas del paciente
            self.lista_paciente.append(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
            
            # Avanza al siguiente sintoma de la enfermedad actual
            self.posicionSintoma+=1
            
            # Comprueba si aun quedan sintomas por preguntar en la enfermedad actual
            if self.posicionSintoma<len(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"]):
                self.generacion_pregunta()
            else:
                #Si ya no hay mas sintomas en esta enfermedad se considera un diagnostico positivo
                self.veredicto("Si")
        elif respuesta=="No":
            
            # Añade el sintoma actual a la lista de sintomas que el paciente NO tiene
            self.lista_NOsintomas.append(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
            self.posicionEnfermedadTemporal=0
            
            # Reinicia los indices para buscar una nueva enfermedad compatible
            self.posicionSintoma=0
            
            # Itera sobre todo el catalogo de enfermedades para encontrar una nueva candidata
            for enfermedad in self.lista_enfermedades:
                
                #Comprueba si la enfermedad actual del bucle CUMPLE con TODOS los sintomas que el paciente SI tiene y NO TIENE NINGUNO de los sintomas que el paciente NO tiene
                if all(sintoma in enfermedad["sintomas"] for sintoma in self.lista_paciente) and all(sintoma not in enfermedad["sintomas"] for sintoma in self.lista_NOsintomas):
                    
                    # Si encuentra una enfermedad compatible actualiza el indice principal a esta nueva enfermedad
                    self.posicionEnfermedad=self.posicionEnfermedadTemporal
                    break
                self.posicionEnfermedadTemporal+=1
            
            # Comprueba si se encontro una nueva enfermedad candidata
            if self.posicionEnfermedadTemporal<len(self.lista_enfermedades):
                self.generacion_pregunta()
            else:
                # Si el bucle termino sin encontrar ninguna enfermedad compatible llama al veredicto
                self.veredicto("No")


    # Metodo para mostrar el resultado final
    def veredicto(self,sino):
        if sino=="Si":

            # Formatea las listas de sintomas a un texto legible
            sintomas_texto = ", ".join(self.lista_paciente)
            sintomas_enfermedad_texot = ",".join(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"])
            
             # Elimina los botones Si y No
            self.botonSI.destroy()
            self.botonNO.destroy()

            #Actualiza la etiqueta con el nombre de la enfermedad para que se muestre el mensaje
            self.texto.configure(text="El paciente es diagnosticado con: " + self.lista_enfermedades[self.posicionEnfermedad]["nombre"] + "\n\n RECOMENDACION \n\n"+self.lista_enfermedades[self.posicionEnfermedad]["recomendacion"] 
                                + "\n\n JUSTIFICACION \n\n Los pacientes del paciente que son: "+sintomas_texto+".\n\n Coinciden con los sintomas de "+self.lista_enfermedades[self.posicionEnfermedad]["nombre"] +" que son:" +sintomas_enfermedad_texot)
        elif sino=="No":

            # Elimina los botones Si y No
            self.botonSI.destroy()
            self.botonNO.destroy()

             #Actualiza la etiqueta con el nombre de la enfermedad para que se muestre el mensaje
            self.texto.configure(text="Los sintomas del paciente no coinciden con el registro de enfermedades respiratorias almacenado")
