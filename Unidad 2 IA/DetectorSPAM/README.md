Descripción General:

Este proyecto implementa un sistema de detección de correos spam utilizando Python, el sistema carga correos desde un archivo CSV (data/correos.csv), crea objetos tipo correo con los datos extraidos del CSV y ejecuta la detección de spam basada en reglas de palabras clave(se analiza el asunto y contenido), reputación del remitente(por palabras que contenga la direccion del remitente), riesgo de links malware(por su extension) y riesgo de archivos adjuntos (por su tipo), y finalmente muestra un conteo sobre los correos originalmente spam y legibles, y los detectados por el sistema para comprobar su correcto funcionamiento.

Estructura del proyecto:

app.py

correo.py

creacion.py

data/
    correos.csv

Contenido del CSV:

direccion del remitente| asunto | contenido | link | adjunto | Spam o Legible

Ejemplo:

premios@ganadineroya.biz|¡Felicitaciones, ganaste un premio!|Has sido seleccionado para recibir un regalo totalmente GRATIS.|http://ganadineroya.biz| |Spam

Reglas para deteccion:

Regla 1.- Activadores de palabras clave:
Si el asunto o contenido o la direccion del remitente contiene palabras relacionadas con promociones, premios, urgencias, recompensas, dar clic,ectc.., se suma 1 punto a la probabilidad de spam por cada palabra sospechosa.

Regla 2.- Reputacion del remitente:
Si el dominio del link del correo o de la direccion del remitente esta en la lista de dominios sospechosos, se suman 2 puntos a la probabilidad de spam.
Regla 3.- Archivos riesgosos:
Si el archivo adjunto es un ejecutable o contenido comprimido se considera riesgoso y por lo tanto se suman 3 puntos a la probabilidad de spam.

(Al final si el correo sumo por lo menos 3 puntos, se considerara "Spam", en caso contrario sera considerado "Legítimo")

Módulos y Clases

app.py.- Archivo principal que ejecuta el flujo del sistema, sus Funciones principales son:

  1.- Llamar a creacion.carga_correos() para cargar los correos desde correos.csv.
  
  2.- Ejecutar comprobar_spam() en cada objeto correo de los almacenados.
  
  3.- Contar y mostrar en consola:
  
  Cantidad de correos Spam y Legítimos originalmente (spam_real).
    
  Cantidad de correos Spam y Legítimos detectados (spam).

Clase

correo.py.- Define la clase correo para la creacion de objetos tipo correo y contiene la logica para la deteccion de correos Spam.

Modulo

creacion.py.- Define la lista donde se almacenaran los objetos correos despues de haberlos creado, para esto usa el archivo CSV (correos.csv)
y extrae los datos para usarlos en la creacion de los objetos correo.

Flujo del Sistema:

1.-Inicio (app.py):

  a.-Llama a creacion.carga_correos() para cargar los correos desde data/correos.csv.
  
  b.-Se crean los objetos correo y se almacenan en lista_correos_app.
  
2.-Detección de Spam:

  a.-Para cada correo en lista_correos_app, se ejecuta correo.comprobar_spam().
  
  b.-Cada correo se clasifica automáticamente como Spam o Legítimo según las reglas definidas.
  
3.-Conteo de correos originales:

  a.-Se recorre la lista y se cuentan cuántos correos eran originalmente Spam o Legítimos (spam_real).
  
  b-Se imprime el resultado en consola.
  
4.-Conteo de correos detectados:

  a.-Se recorre nuevamente la lista y se cuentan cuántos correos fueron detectados como Spam o Legítimos (spam).

  b.-Se imprime el resultado en consola.

5.-Resultado final:

  a.-Permite comparar cuántos correos fueron correctamente clasificados y detectar posibles falsos positivos o falsos negativos.




