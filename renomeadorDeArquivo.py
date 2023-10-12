import os

pasta = '/caminho/para/sua/pasta'  # Substitua pelo caminho da sua pasta
prefixo = 'a_'

# Verifica se a pasta existe
if os.path.exists(pasta):
    # Lista os arquivos na pasta
    arquivos = os.listdir(pasta)
    contador = 1

    # Itera sobre os arquivos na pasta
    for arquivo in arquivos:
        # Cria o novo nome do arquivo com o prefixo e o contador
        novo_nome = f'{prefixo}{contador}{os.path.splitext(arquivo)[1]}'

        # Gera o caminho completo do arquivo atual
        caminho_atual = os.path.join(pasta, arquivo)

        # Gera o caminho completo do novo arquivo
        novo_caminho = os.path.join(pasta, novo_nome)

        # Renomeia o arquivo
        os.rename(caminho_atual, novo_caminho)

        # Incrementa o contador
        contador += 1

    print('Arquivos renomeados com sucesso!')
else:
    print('A pasta não existe.')