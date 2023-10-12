import tensorflow as tf
from keras import layers, models
from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np
from Imagens import Imagens, TipoImagem

# Pega os diretórios onde estão localizadas as pastas de treino e teste para formatá-las no modelo correto
dir_imagem_treino = r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\train_images\formatoPNG'
dir_imagem_teste = r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\test_images\formatoPNG'

imagens = Imagens()

imagens.Formata_imagem_e_rotulos(dir_imagem_treino, TipoImagem.treino)
imagens.Formata_imagem_e_rotulos(dir_imagem_teste, TipoImagem.teste)


# Pega as imagens do tipo npy e as carrega para dentro de variáveis
train_images = np.load(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\train_images\formatoNumpy\train_images_npy.npy')
train_labels = np.load(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\train_labels\formatoNumpy\train_labels_npy.npy')
test_images = np.load(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\test_images\formatoNumpy\test_images_npy.npy')
test_labels = np.load(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\test_labels\formatoNumpy\test_labels_npy.npy')

print(len(train_images))
print(len(train_labels))
print(len(test_images))
print(len(test_labels))

# Pré-processamento dos dados (transforma em tons de cinza, dps garante a dimensão da imagem)
train_images = np.mean(train_images, axis=-1, keepdims=True)
train_images = train_images.reshape((1009, 28, 28, 1))
test_images = np.mean(test_images, axis=-1, keepdims=True)
test_images  = test_images.reshape((512, 28, 28, 1))
train_images, test_images = train_images / 255.0, test_images / 255.0

train_labels = train_labels.astype(int)
test_labels = test_labels.astype(int)

# Construir o modelo da rede neural
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

# Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Treinar o modelo
history = model.fit(train_images, train_labels, epochs=10,
                    validation_data=(test_images, test_labels))

# Avaliar o desempenho do modelo
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nAcurácia do modelo no conjunto de teste:', test_acc)

# Plotar a acurácia e a perda ao longo do treinamento
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Acurácia de Treinamento')
plt.plot(history.history['val_accuracy'], label='Acurácia de Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Perda de Treinamento')
plt.plot(history.history['val_loss'], label='Perda de Validação')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend()

plt.show()

model.save(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\tcc_7_sem\tcc_8_sem\model_letra_teste.h5')
