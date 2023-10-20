import os
import cv2
import numpy as np
from enum import Enum
from keras.models import load_model


class Letra(Enum):
    A = 1
    B = 2
    C = 3
    D = 4
    E = 5
    F = 6
    G = 7
    H = 8
    I = 9
    J = 10
    K = 11
    L = 12
    M = 13
    N = 14
    O = 15
    P = 16
    Q = 17
    R = 18
    S = 19
    T = 20
    U = 21
    V = 22
    W = 23
    X = 24
    Y = 25
    Z = 26




class RetornaClasse:
    # Carregue o modelo treinado
    arquivoModelo = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'RedeNeural', 'model_letra_teste.h5')
    modeloCarregado = load_model(arquivoModelo)  # Substitua pelo caminho do seu modelo treinado

    # Função para fazer previsões em uma imagem
    @staticmethod
    def prever_letra(imagem):
        try:
            imagem = cv2.imread(imagem, cv2.IMREAD_GRAYSCALE)
            imagem = cv2.resize(imagem, (28, 28))
            imagem = np.invert(imagem)
            imagem = imagem.reshape(1, 28, 28, 1).astype('float32') / 255.0

            # Faça a previsão
            predicao = RetornaClasse.modeloCarregado.predict(imagem)
            predicaoClasse = np.argmax(predicao, axis=1)
            retornaLetra = Letra(predicaoClasse[0]).name
            return retornaLetra
        except:
            raise Exception("Não foi possível ler a imagem.")