import tensorflow as tf
import cv2
import numpy as np
import json
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import mediapipe as mp

#Aqui se carga el modelo que ya entrenamos como se podra dar cuenta profe
#el mejor y no el otro
modelo = tf.keras.models.load_model("mejor_modelo.h5")

#Aaqui se cargan las clases del .JSON que se genero
with open("clases.json", "r") as f:
    clases_indices = json.load(f)
#y se invierte para que se muestre correctamente la emocion y su porcentaje
clases = {v: k for k, v in clases_indices.items()}

#Aqui se incializa MediaPipe Face Detection para ayudar con lo de la camara
mp_detector = mp.solutions.face_detection
detector = mp_detector.FaceDetection(model_selection=0, min_detection_confidence=0.5)

#Aqui ajui se inicializa la camara y se ajusta la resolucion
camara = cv2.VideoCapture(0)
camara.set(3, 640)
camara.set(4, 480)

print("Presiona 'ESC' para salir")


##En este While es donde se hace la chamba para la deteccion en tiempo real
while True:
    ret, frame = camara.read()
    if not ret:
        break
    #Se pasa a RGB porque asi trabaja MEdiapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    ##Se procesa la deteccion del rostro
    resultados = detector.process(frame_rgb)

#En caso de que se logre detectar un rostro se mantiene iterando en ese
    if resultados.detections:
        for deteccion in resultados.detections:
            h, w, _ = frame.shape
            bbox = deteccion.location_data.relative_bounding_box
            ## El MediaPipe devuelve coordenadas relativas y estas ps se convierten a pixeles
            x1 = int(bbox.xmin * w)
            y1 = int(bbox.ymin * h)
            x2 = int((bbox.xmin + bbox.width) * w)
            y2 = int((bbox.ymin + bbox.height) * h)

            #Se agrega padding para que no quede muy recortado el rostro de mas
            padding = 20
            x1 = max(0, x1 - padding)
            y1 = max(0, y1 - padding)
            x2 = min(w, x2 + padding)
            y2 = min(h, y2 + padding)

            #Se recorta acordemente el rostro
            cara = frame[y1:y2, x1:x2]
             
            ##Aqui se valida que sea valido
            if cara.size == 0:
                continue

            #Aqui se hace el Preprocesamiento
            cara_rgb = cv2.cvtColor(cara, cv2.COLOR_BGR2RGB)
            cara_reescalada = cv2.resize(cara_rgb, (224, 224))
            cara_input = preprocess_input(cara_reescalada)
            cara_input = np.expand_dims(cara_input, axis=0)

            #Aqui se haca la Predicción
            prediccion = modelo.predict(cara_input, verbose=0)
            clases_id = np.argmax(prediccion)
            confianza = np.max(prediccion)
            clases_nombre = clases[clases_id]

            #Aqui se Dibujan el recuadro que enmarcara la cara y los resultados sobre dicho recuadro
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{clases_nombre} ({confianza*100:.1f}%)",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (0, 255, 0), 2)
 ##Pa mostrar la ventana en pantalla
    cv2.imshow("Detector de Emociones", frame)

    ##Esto es para poder salir de la app
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
##Aqui Se liberan los recuros
camara.release()
cv2.destroyAllWindows()
