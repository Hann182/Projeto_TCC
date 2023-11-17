import os

import numpy as np
import matplotlib.pyplot as plt
from keras import layers, models
from Imagens import Imagens, TipoImagem

# Pega os diretórios onde estão localizadas as pastas de treino e teste para formatá-las no modelo correto
caminho_treino_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'train_images')
caminho_teste_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'test_images')
caminho_treino_labels = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'train_labels')
caminho_teste_labels = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'test_labels')

dir_imagem_treino = os.path.join(caminho_treino_imagens, 'formatoPNG')
dir_imagem_teste = os.path.join(caminho_teste_imagens, 'formatoPNG')

imagens = Imagens()

imagens.formataImagemERotulo(dir_imagem_treino, TipoImagem.treino)
imagens.formataImagemERotulo(dir_imagem_teste, TipoImagem.teste)


# Pega as imagens do tipo npy e as carrega para dentro de variáveis
imagens_treino = np.load(os.path.join(caminho_treino_imagens, 'formatoNumpy', 'train_images_npy.npy'))
labels_treino = np.load(os.path.join(caminho_treino_labels, 'formatoNumpy', 'train_labels_npy.npy'))
imagens_teste = np.load(os.path.join(caminho_teste_imagens, 'formatoNumpy', 'test_images_npy.npy'))
labels_teste = np.load(os.path.join(caminho_teste_labels, 'formatoNumpy', 'test_labels_npy.npy'))

'''print(len(imagens_treino))
print(len(labels_treino))
print(len(imagens_teste))
print(len(labels_teste))'''

# Pré-processamento dos dados (transforma em tons de cinza, dps garante a dimensão da imagem)
imagens_treino = np.mean(imagens_treino, axis=-1, keepdims=True)
imagens_treino = imagens_treino.reshape((6488, 28, 28, 1))
imagens_teste = np.mean(imagens_teste, axis=-1, keepdims=True)
imagens_teste = imagens_teste.reshape((2655, 28, 28, 1))
imagens_treino, imagens_teste = imagens_treino / 255.0, imagens_teste / 255.0

labels_treino = labels_treino.astype(int)
labels_teste = labels_teste.astype(int)

# Construir o modelo da rede neural
modelo = models.Sequential()
modelo.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
modelo.add(layers.MaxPooling2D((2, 2)))
modelo.add(layers.Conv2D(64, (3, 3), activation='relu'))
modelo.add(layers.MaxPooling2D((2, 2)))
modelo.add(layers.Conv2D(64, (3, 3), activation='relu'))
modelo.add(layers.Flatten())
modelo.add(layers.Dense(64, activation='relu'))
modelo.add(layers.Dense(27, activation='softmax'))

# Compilar o modelo
modelo.compile(optimizer='adam',
               loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])

# Treinar o modelo
historico = modelo.fit(imagens_treino, labels_treino, epochs=10,
                     validation_data=(imagens_teste, labels_teste))

# Avaliar o desempenho do modelo
test_loss, test_acc = modelo.evaluate(imagens_teste, labels_teste, verbose=2)
print('\nAcurácia do modelo no conjunto de teste:', test_acc)

# Plotar a acurácia e a perda ao longo do treinamento
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(historico.history['accuracy'], label='Acurácia de Treinamento')
plt.plot(historico.history['val_accuracy'], label='Acurácia de Validação')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(historico.history['loss'], label='Perda de Treinamento')
plt.plot(historico.history['val_loss'], label='Perda de Validação')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend()

plt.show()

modelo.save(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'RedeNeural', 'model_letra_teste.h5'))
