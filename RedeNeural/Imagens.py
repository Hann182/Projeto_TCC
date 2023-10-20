import os
import numpy as np
from PIL import Image
from enum import Enum

class TipoImagem(Enum):
    treino = 1
    teste = 2

class Imagens():

    caminhoTreinoImagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'train_images')
    caminhoTesteImagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'test_images')
    caminhoTreinoLabels = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories','ImagensDaRedeNeural', 'train_labels')
    caminhoTesteLabels = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'ImagensDaRedeNeural', 'test_labels')

    # Crie listas para armazenar as imagens e rótulos
    def Formata_imagem_e_rotulos(self, diretorio_raiz, tipoImagem):
        imagens = []
        rotulos = []

        # Itere sobre as pastas (cada pasta representa uma classe)
        for classe in os.listdir(diretorio_raiz):
            pasta_da_classe = os.path.join(diretorio_raiz, classe)
            if os.path.isdir(pasta_da_classe):
                for arquivo in os.listdir(pasta_da_classe):
                    if arquivo.endswith('.png'):
                        caminho_da_imagem = os.path.join(pasta_da_classe, arquivo)
                        imagem = Image.open(caminho_da_imagem)
                        imagem = imagem.resize((28, 28))  # Redimensione para 28x28 se necessário
                        imagem_array = np.array(imagem)
                        imagens.append(imagem_array)
                        rotulos.append(classe)


        # Converta as listas em matrizes NumPy
        imagens = np.array(imagens)
        rotulos = np.array(rotulos)

        # Salvando na pasta devida
        if(tipoImagem == TipoImagem.treino):
            np.save(os.path.join(Imagens.caminhoTreinoImagens, 'formatoNumpy', 'train_images_npy'), imagens)
            np.save(os.path.join(Imagens.caminhoTreinoLabels, 'formatoNumpy', 'train_labels_npy'), rotulos)

        elif(tipoImagem == TipoImagem.teste):
            np.save(os.path.join(Imagens.caminhoTesteImagens, 'formatoNumpy', 'test_images_npy'), imagens)
            np.save(os.path.join(Imagens.caminhoTesteLabels, 'formatoNumpy', 'test_labels_npy'), rotulos)

