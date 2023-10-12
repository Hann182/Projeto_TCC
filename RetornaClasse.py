import tensorflow as tf
from keras.models import load_model
import numpy as np
import cv2

# Carregue o modelo treinado
model = load_model(r'D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\tcc_7_sem\tcc_8_sem\model_letra_teste.h5')  # Substitua pelo caminho do seu modelo treinado


# Função para fazer previsões em uma imagem
def prever_letra(imagem):
    # Carregue a imagem e pré-processamento
    imagem = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)
    imagem = cv2.resize(imagem, (28, 28))
    imagem = np.invert(imagem)
    imagem = imagem.reshape(1, 28, 28, 1).astype('float32') / 255.0

    # Faça a previsão
    pred = model.predict(imagem)
    predClass = np.argmax(pred, axis=1)
    return predClass


# Insira o caminho da imagem que você deseja classificar
caminho_da_imagem = r"D:\B - UNIP\8 - Semestre\0 - Trabalho de curso II\letras\classificacao\a3.png"
classe_predita = prever_letra(caminho_da_imagem)

print(f'A classe predita para a imagem é: {classe_predita}')


#