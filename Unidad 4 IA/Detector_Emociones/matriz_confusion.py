import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import DepthwiseConv2D 
from sklearn.metrics import classification_report, confusion_matrix

#CONFIGURACIÓN
RUTA_MODELO = 'mejor_modelo.h5' 
RUTA_DATASET = 'dataset'       
IMG_TAM = (224, 224)
BATCH_TAM = 32

def evaluar():
    print(f"Cargando modelo desde: {RUTA_MODELO}...")
    

    class CustomDepthwiseConv2D(DepthwiseConv2D):
        def __init__(self, **kwargs):
            kwargs.pop('groups', None) 
            super().__init__(**kwargs)


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

    #Preparar generador
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

    #Predicciones
    print("Realizando predicciones...")
    predicciones = modelo.predict(valor_generador, verbose=1)
    
    y_pred = np.argmax(predicciones, axis=1)
    y_true = valor_generador.classes
    clases_nombres = list(valor_generador.class_indices.keys())

    #Matriz de Confusión
    confusion = confusion_matrix(y_true, y_pred)

    plt.figure(figsize=(10, 8))
    sns.heatmap(confusion, annot=True, fmt='d', cmap='Blues', 
                xticklabels=clases_nombres, yticklabels=clases_nombres)
    plt.title('Matriz de Confusión')
    plt.ylabel('Etiqueta Real')
    plt.xlabel('Predicción')
    plt.tight_layout()
    plt.show()

    #Reporte
    print("\n--- REPORTE DE CLASIFICACIÓN ---")
    print(classification_report(y_true, y_pred, target_names=clases_nombres))

if __name__ == "__main__":
    evaluar()