Link del Google Drive (donde se encuentran el Dataset, el mejor modelo generado, el modelo final que puede ser o no el mejor, las clases [osea las emociones] en un .JSON y el VIDEO testeando el modelo):

https://drive.google.com/drive/folders/1dFyUTqx9YDUuG0sxlsJ4v_gjZAmBc5zD?usp=sharing

Link directo del Video que esta en el Drive:

https://drive.google.com/file/d/1v3Ut_UjAkcL8Lezs9rVMhijRdZAyqHXP/view?usp=sharing

📷 SISTEMA DE DETECCIÓN DE EMOCIONES CON DEEP LEARNING Y RECONOCIMIENTO FACIAL EN TIEMPO REAL

Elaborado por:

👨‍💻 Jonatan Arnoldo Valdez Ayala

👨‍💻 Jose Enrique Espindola Leyva

📄 DESCRIPCIÓN

Este proyecto implementa un Sistema de Reconocimiento de Emociones basado en Deep Learning, utilizando el modelo preentrenado MobileNetV2, ajustado mediante transfer learning para clasificar cuatro emociones faciales: Feliz, Triste, Enojado y Neutral.

El sistema trabaja con tres componentes principales:

🧠 Un script de entrenamiento para generar el modelo.

📊 Un módulo de evaluación con matriz de confusión.

🎥 Una aplicación en tiempo real que detecta el rostro y predice la emoción usando la cámara web.

La detección facial se realiza con MediaPipe, mientras que el análisis emocional se ejecuta con TensorFlow/Keras y el modelo entrenado.

⚙️ FUNCIONALIDADES

🔹 1. Entrenamiento del Modelo (entrenamiento.py)

Uso de MobileNetV2 como red base para transfer learning.

Preprocesamiento de imágenes con ImageDataGenerator.

Entrenamiento en dos fases (capas congeladas y descongeladas).

Guardado automático del mejor modelo (mejor_modelo.h5).

Generación de archivo JSON con las clases del dataset.

🔹 2. Detección en Tiempo Real (camara.py)

Activación de la cámara mediante OpenCV.

Detección del rostro con MediaPipe Face Detection.

Recorte, reescalado y preprocesamiento de la cara detectada.

Predicción de emoción en tiempo real con el modelo entrenado.

Visualización en pantalla del recuadro facial y porcentaje de confianza.

Finalización con la tecla "ESC".

🔹 3. Análisis del Modelo (matriz_confusion.py)

Carga del modelo y las clases usando MobileNetV2.

Evaluación del conjunto de validación del dataset.

Generación automática de:

📊 Matriz de confusión

🧾 Reporte de clasificación (precision, recall, f1-score)


▶️ EJECUCIÓN

📘 La ejecución se divide de la siguiente forma:

Para entrenar el modelo:
python entrenamiento.py

Para analizar el rendimiento del modelo:
python matriz_confusion.py

Para usar la cámara y detectar emociones en tiempo real:
python camara.py
