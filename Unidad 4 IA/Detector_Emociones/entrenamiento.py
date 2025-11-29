from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
import tensorflow as tf
import json


#Cargar MobileNetV2 sin la parte final
modelo = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224,224,3))
modelo.trainable = False  # Congela MobileNetV2 (fase 1)


# Cargar imágenes con split de validación
aumentacion = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1,
    brightness_range=[0.8,1.2],
    horizontal_flip=True,
    validation_split=0.2
)

imagenes_entrenar = aumentacion.flow_from_directory(
    'dataset',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    color_mode='rgb',
    subset='training'
)

imagenes_validar = aumentacion.flow_from_directory(
    'dataset',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    color_mode='rgb',
    subset='validation'
)


# Crear la cabeza del modelo
cabeza_modelo = modelo.output
cabeza_modelo = GlobalAveragePooling2D()(cabeza_modelo)
cabeza_modelo = Dense(128, activation='relu')(cabeza_modelo)
predictions = Dense(imagenes_entrenar.num_classes, activation='softmax')(cabeza_modelo)

model = Model(inputs=modelo.input, outputs=predictions)


#Compilar para la fase 1 (congelado)
model.compile(
    optimizer=Adam(learning_rate=1e-4),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


#CALLBACKS
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.3,
    patience=3,
    min_lr=1e-6
)

checkpoint = ModelCheckpoint(
    "mejor_modelo.h5",
    monitor="val_loss",
    save_best_only=True
)


#FASE 1: solo cabeza del modelo
print("===== ENTRENANDO FASE 1 (base congelada) =====")
model.fit(
    imagenes_entrenar,
    validation_data=imagenes_validar,
    epochs=25,
    callbacks=[early_stop, reduce_lr, checkpoint]
)


#FASE 2: fine-tuning (descongelar últimas capas)
print("===== ENTRENANDO FASE 2 (fine-tuning) =====")

tf.keras.backend.clear_session()

for layer in modelo.layers[:-40]:   # congela todo excepto las últimas 40 capas
    layer.trainable = False

for layer in modelo.layers[-40:]:   # últimas 40 capas sí entrenan
    layer.trainable = True

# recompilar con LR más bajo
model.compile(
    optimizer=Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    imagenes_entrenar,
    validation_data=imagenes_validar,
    epochs=30,
    callbacks=[early_stop, reduce_lr, checkpoint]
)



#Guardar modelo final
model.save("modelo_entrenado.h5")


#Guardar nombres de clases
with open("clases.json", "w") as f:
    json.dump(imagenes_entrenar.class_indices, f)

print("Entrenamiento finalizado y modelo guardado.")