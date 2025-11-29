import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import DepthwiseConv2D 
from sklearn.metrics import classification_report, confusion_matrix

#Se haace la configuracion, definiendo el modelo y dataset a usar (ponemos su ruta)
# ademas el tamanio a usar de imagen (el que acepta MobileNetV2) y el tamanio de los lotes de imagenes
RUTA_MODELO = 'mejor_modelo.h5' 
RUTA_DATASET = 'dataset'       
IMG_TAM = (224, 224)
BATCH_TAM = 32

def evaluar():
    print(f"Cargando modelo desde: {RUTA_MODELO}...")
    
    # Cuando se carga MobileNetV2 en algunas versiones aparece un argumento "groups" que no existe en DepthwiseConv2D.
    # Es por eso que CustomDepthwiseConv2D elimina ese argumento para permitir que el modelo cargue correctamente.

    class CustomDepthwiseConv2D(DepthwiseConv2D):
        def __init__(self, **kwargs):
            kwargs.pop('groups', None) 
            super().__init__(**kwargs)

    # Se Carga el modelo incluyendo la clase personalizada 
    # esto evita errores al estar reconstruiyebd capas específicas
    try:
        # Pasar la clase personalizada en custom_objects
        modelo = tf.keras.models.load_model(
            RUTA_MODELO, 
            custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D}
        )
        print("¡Modelo cargado exitosamente!")
    except Exception as e:
        print(f"Error fatal al cargar: {e}")
        return

    #Aqui se prepara el generador para la validacion de imagenes
    test_generador = ImageDataGenerator(
        preprocessing_function=preprocess_input,
        validation_split=0.2 
    )

    print("Preparando imágenes de validación...")
    valor_generador = test_generador.flow_from_directory(
        RUTA_DATASET,
        target_size=IMG_TAM,
        batch_size=BATCH_TAM,
        class_mode='categorical',
        subset='validation',
        shuffle=False
    )

    #Aqui se realizan Predicciones sobre las imagenes de validaacion
    #el modelo devuelve 1 por clase
    print("Realizando predicciones...")
    predicciones = modelo.predict(valor_generador, verbose=1)
    
    y_pred = np.argmax(predicciones, axis=1)
    y_true = valor_generador.classes
    clases_nombres = list(valor_generador.class_indices.keys())

    #Aqui se genera la Matriz de Confusión la cual nos dice cuantas imagenes
    #acerto el modelo o cuantas confundio incluso
    confusion = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(10, 8))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', 
                xticklabels=clases_nombres, yticklabels=clases_nombres)
    plt.title('Matriz de Confusión')
    plt.ylabel('Etiqueta Real')
    plt.xlabel('Predicción')
    plt.tight_layout()
    plt.show()

    # Aqui se hace el reporte de clasificación:
    # donde se muestra precisión, recall y f1-score para cada clase.
    print("\n--- REPORTE DE CLASIFICACIÓN ---")
    print(classification_report(y_true, y_pred, target_names=clases_nombres))


if __name__ == "__main__":
    evaluar()