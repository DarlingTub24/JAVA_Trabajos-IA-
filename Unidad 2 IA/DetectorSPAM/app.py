import creacion
##Se cargan los correos para crear objetos correo con sus datos
## y se almacenan en lista_correos, luego se hace la deteccion
creacion.carga_correos()
lista_correos_app=creacion.lista_correos
for correo in lista_correos_app:
    correo.comprobar_spam()
##Se hace recuento de cuantos correos eran Spam o Legibles en un inicio
## y se imprime
conteo_spam=0
conteo_legible=0
for correo in lista_correos_app:
    if correo.spam_real == "Spam":
        conteo_spam+=1
    else:
        conteo_legible+=1
print("Cantidad de Correos Spam originalmente:")
print(conteo_spam)
print("Cantidad de Correos Legibles originalmente:")
print(conteo_legible)
##Se hace recuento de cuantos correos Spam y Legibles se detectaron
## y se imprime
conteo_spam=0
conteo_legible=0
for correo in lista_correos_app:
    if correo.spam == "Spam":
        conteo_spam+=1
    else:
        conteo_legible+=1
print("Cantidad de Correos Spam detectados:")
print(conteo_spam)
print("Cantidad de Correos Legibles detectados:")
print(conteo_legible)

