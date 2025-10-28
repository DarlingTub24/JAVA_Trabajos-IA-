import tkinter as tk
import Sistema_Experto
class LoginInterfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Sistema Experto")
        width = 400
        height = 400
        x = (self.ventana.winfo_screenwidth() - width) // 2
        y = (self.ventana.winfo_screenheight() - height) // 2
        self.ventana.geometry(f"{width}x{height}+{x}+{y}")
        self.ventana.rowconfigure(0,weight=1)
        self.ventana.rowconfigure(4,weight=1)
        self.lista_enfermedades=Sistema_Experto.catalogo_Enfermedades
        self.lista_paciente=[]
        self.lista_NOsintomas=[]
        self.texto= tk.Label(self.ventana,text="",wraplength=350,justify="center")
        self.texto.grid(row=1,column=0,padx=0,pady=10,sticky="ew")
        self.ventana.columnconfigure(0,weight=1)
        self.botonSI= tk.Button(self.ventana,text="Si",command=lambda: self.respuesta("Si"))
        self.botonSI.grid(row=2,column=0,padx=0,pady=10,sticky="ew")
        self.botonNO= tk.Button(self.ventana,text="No",command=lambda: self.respuesta("No"))
        self.botonNO.grid(row=3,column=0,padx=0,pady=10,sticky="ew")
        self.posicionSintoma=0
        self.posicionEnfermedad=0
        self.posicionEnfermedadTemporal=0
        self.generacion_pregunta()

    def generacion_pregunta(self):
        if self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma] not in self.lista_NOsintomas and self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma] not in self.lista_paciente:
            self.texto.configure(text="Usted Presenta el Siguiente Sintoma: " + self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
        else:
            self.posicionSintoma+=1
            self.generacion_pregunta()
    def respuesta(self,respuesta):
        if respuesta=="Si":
            self.lista_paciente.append(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
            self.posicionSintoma+=1
            if self.posicionSintoma<len(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"]):
                self.generacion_pregunta()
            else:
                self.veredicto("Si")
        elif respuesta=="No":
            self.lista_NOsintomas.append(self.lista_enfermedades[self.posicionEnfermedad]["sintomas"][self.posicionSintoma])
            self.posicionEnfermedadTemporal=0
            self.posicionSintoma=0
            for enfermedad in self.lista_enfermedades:
                if all(sintoma in enfermedad["sintomas"] for sintoma in self.lista_paciente) and all(sintoma not in enfermedad["sintomas"] for sintoma in self.lista_NOsintomas):
                    self.posicionEnfermedad=self.posicionEnfermedadTemporal
                    break
                self.posicionEnfermedadTemporal+=1
            if self.posicionEnfermedadTemporal<len(self.lista_enfermedades):
                self.generacion_pregunta()
            else:
                self.veredicto("No")

    def veredicto(self,sino):
        if sino=="Si":
            self.botonSI.destroy()
            self.botonNO.destroy()
            self.texto.configure(text="El paciente es diagnosticado con: " + self.lista_enfermedades[self.posicionEnfermedad]["nombre"])
        elif sino=="No":
            self.botonSI.destroy()
            self.botonNO.destroy()
            self.texto.configure(text="Los sintomas del paciente no coinciden con el registro de enfermedades respiratorias almacenado")


