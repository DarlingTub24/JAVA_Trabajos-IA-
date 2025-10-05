import correo
lista_correos=[]
##Este metodo se encarga de abrir el archivo "correos.csv" de la carpeta "data/"
##recorre todos sus renglones y separando en base a "|" se dedica a almacenar
##el contenido de cada linea, y usandolo crea los correos como objetos y los almacena
##en "lista_correos".
def carga_correos(archivo="data/correos.csv"):
    with open(archivo,"r",encoding="utf-8") as datos:
        for linea in datos:
            partes=linea.strip().split("|")
            remitente=partes[0].strip()
            asunto=partes[1].strip()
            contenido=partes[2].strip()
            link=partes[3].strip()
            adjunto=partes[4].strip()
            spam=partes[5].strip()
            correo_actual=correo.correo(remitente,asunto,contenido,link,adjunto,spam)
            lista_correos.append(correo_actual)

