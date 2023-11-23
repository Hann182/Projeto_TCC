import cv2, sys, os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from RedeNeural.RetornaClasse import RetornaClasse
from JanelaEspessura import JanelaEspessura
from JanelaLetraPontilhada import JanelaLetraPontilhada

lista_de_letras = [] 
     
class Window(QMainWindow):  
    def __init__(self):
        super().__init__()

        self.minha_lista = []
        self.last_point = None
        self.status_borracha = False

        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        self.setWindowTitle("Tela Digitalizadora")
        self.setFixedSize(900, 630)
        self.setStyleSheet("background-color: #CAE3FB;")
        self.setWindowIcon(QIcon(os.path.join(caminho_pasta_imagens, 'download.png')))

        self.image = QPixmap(300, 300)
        self.image.fill(QColor("#ffffff"))
    
        self.background_botoes = QLabel(self)
        self.background_botoes.setGeometry(QRect(5, 30, 45, 590))
        self.background_botoes.setStyleSheet(u"background-color:#DEEFF6; border-radius: 5px")
        
        self.borda_topo = QLabel(self)
        self.borda_topo.setGeometry(QRect(315, 320, 300, 1))
        self.borda_topo.setStyleSheet(u"background-color:#808080")
        
        self.borda_baixo = QLabel(self)
        self.borda_baixo.setGeometry(QRect(315, 620, 300, 1))
        self.borda_baixo.setStyleSheet(u"background-color:#808080")
        
        self.borda_esquerda = QLabel(self)
        self.borda_esquerda.setGeometry(QRect(315, 320, 1, 300))
        self.borda_esquerda.setStyleSheet(u"background-color:#808080")
        
        self.borda_direita = QLabel(self)
        self.borda_direita.setGeometry(QRect(615, 320, 1, 301))
        self.borda_direita.setStyleSheet(u"background-color:#808080")

        self.tela_digitalizada = QTextBrowser(self)
        self.tela_digitalizada.setObjectName(u"tela_digitalizada")
        self.tela_digitalizada.setGeometry(QRect(55, 30, 830, 275))
        self.tela_digitalizada.setAutoFillBackground(False)
        self.tela_digitalizada.setStyleSheet(u"background-color:#ffffff; border: 1px solid gray")

#botões da tela de cima (digitalizada)
        self.botao_exportar_texto = QPushButton(self)
        self.botao_exportar_texto.setGeometry(10, 40, 35, 35)
        self.botao_exportar_texto.clicked.connect(self.salvarDocumento)
        self.botao_exportar_texto.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'salvar_arquivo_como_texto.png')))
        self.botao_exportar_texto.setIconSize(QSize(30, 30))
        self.botao_exportar_texto.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_apagar_letra_digitalizada = QPushButton(self)
        self.botao_apagar_letra_digitalizada.setGeometry(10, 85, 35, 35)
        self.botao_apagar_letra_digitalizada.clicked.connect(self.apagarLetra)
        self.botao_apagar_letra_digitalizada.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'borracha_escrita.png')))
        self.botao_apagar_letra_digitalizada.setIconSize(QSize(40, 40))
        self.botao_apagar_letra_digitalizada.setStyleSheet(u"background-color:#ffffff")

        self.botao_digitalizar = QPushButton(self)
        self.botao_digitalizar.setGeometry(10, 130, 35, 35)
        self.botao_digitalizar.clicked.connect(self.digitalizar)
        self.botao_digitalizar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'print.png')))
        self.botao_digitalizar.setIconSize(QSize(30, 30))
        self.botao_digitalizar.setStyleSheet(u"background-color:#ffffff")

        self.botao_abrir_novo_documento = QPushButton(self)
        self.botao_abrir_novo_documento.setGeometry(10, 175, 35, 35)
        self.botao_abrir_novo_documento.clicked.connect(self.abrirNovoDocumento)
        self.botao_abrir_novo_documento.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'novo_documento.png')))
        self.botao_abrir_novo_documento.setIconSize(QSize(30, 30))
        self.botao_abrir_novo_documento.setStyleSheet(u"background-color:#ffffff")

        self.borda_direita = QLabel(self)
        self.borda_direita.setGeometry(QRect(5, 230, 45, 1))
        self.borda_direita.setStyleSheet(u"background-color:#CAE3FB")

#botões da tela de baixo (desenho)
        self.botao_lapis = QPushButton(self)
        self.botao_lapis.setGeometry(10, 285, 35, 35)
        self.botao_lapis.clicked.connect(self.lapis)
        self.botao_lapis.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'lapis.png')))
        self.botao_lapis.setIconSize(QSize(30, 30))
        self.botao_lapis.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_borracha = QPushButton(self)
        self.botao_borracha.setGeometry(10, 330, 35, 35)
        self.botao_borracha.clicked.connect(self.borracha)
        self.botao_borracha.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'borracha_lapis.png')))
        self.botao_borracha.setIconSize(QSize(30, 30))
        self.botao_borracha.setStyleSheet(u"background-color:#ffffff")

        self.botao_limpar = QPushButton(self)
        self.botao_limpar.setGeometry(10, 375, 35, 35)
        self.botao_limpar.clicked.connect(self.limparTela)
        self.botao_limpar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'limpar.png')))
        self.botao_limpar.setIconSize(QSize(30, 30))
        self.botao_limpar.setStyleSheet(u"background-color:#ffffff")

        self.botao_escolher_cor = QPushButton(self)
        self.botao_escolher_cor.setGeometry(10, 420, 35, 35)
        self.botao_escolher_cor.clicked.connect(self.mostrarCor)
        self.botao_escolher_cor.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'cor.png')))
        self.botao_escolher_cor.setIconSize(QSize(30, 30))
        self.botao_escolher_cor.setStyleSheet(u"background-color:#ffffff")

        self.botao_espessura = QPushButton(self)
        self.botao_espessura.setGeometry(10, 465, 35, 35)
        self.botao_espessura.clicked.connect(self.mostrarEspessuraLapis)
        self.botao_espessura.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'espessura.png')))
        self.botao_espessura.setIconSize(QSize(30, 30))
        self.botao_espessura.setStyleSheet(u"background-color:#ffffff")

        self.botao_letra_pontilhada = QPushButton(self)
        self.botao_letra_pontilhada.setGeometry(10, 510, 35, 35)
        self.botao_letra_pontilhada.clicked.connect(self.mostrarLetraPontilhada)
        self.botao_letra_pontilhada.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'pontilhado.png')))
        self.botao_letra_pontilhada.setIconSize(QSize(30, 30))
        self.botao_letra_pontilhada.setStyleSheet(u"background-color:#ffffff")
        
        self.label = QLabel(self)
        self.drawing = False
        self.brush_size = 10
        self.brush_color = QColor("#000000")
        self.lastPoint = QPoint()

        self.mouse_release_timer = QTimer(self)
        self.mouse_release_timer.setSingleShot(True)
        self.mouse_release_timer.timeout.connect(self.afterMouseRelease)

    def mousePressEvent(self, event):
        current_point = event.pos() - QPoint(315, 320)
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = current_point

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            current_point = event.pos() - QPoint(315, 320)
            painter.drawLine(self.lastPoint, current_point)
            self.lastPoint = current_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.mouse_release_timer.start(2500)
            

    @pyqtSlot()
    def afterMouseRelease(self):
        if self.status_borracha == True:
            print(self.status_borracha)
        else:
            print(self.status_borracha)
            self.digitalizar()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(315, 320, self.image)

    def salvar(self):
        caminho_arquivo, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if caminho_arquivo == "":
            return self.image.save(caminho_arquivo)

    def digitalizar(self):
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')

        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(caminho_screenshot, 'png')

        imagem = cv2.imread(caminho_screenshot)
        cortar_screenshot = imagem[320:620, 315:615]
        cv2.imwrite(caminho_screenshot, cortar_screenshot)
        self.pixmap = QPixmap(caminho_screenshot)
        self.retornarTextoImagem()
        
    def limparTela(self):
        self.image.fill(Qt.white)
        self.update()

    def abrirImagem(self):
        opcoes = QFileDialog.Options()
        nome_arquivo, _ = QFileDialog.getOpenFileName(self, 'Abrir Imagem', '',
                                                   'Imagens (*.png *.jpg *.jpeg *.gif *.bmp);;Todos os Arquivos (*)',
                                                   options=opcoes)
        if nome_arquivo:
            imagem_na_tela_label = QPixmap(nome_arquivo)
            self.setarImagem(imagem_na_tela_label)

    def setarImagem(self, imagem_na_tela_label):
        if not imagem_na_tela_label.isNull():
            self.image = imagem_na_tela_label.scaled(300, 300, Qt.KeepAspectRatio)
            self.update()

    def mostrarCor(self):
        cor = QColorDialog.getColor(initial=self.brush_color)
        
        if cor.isValid():
            self.brush_color = cor
            
    def borracha(self):
        self.status_borracha = True
        self.brush_color = QColor("#FFFFFF")

    def lapis(self):
        self.status_borracha = False
        self.brush_color = QColor("#000000")

    def mostrarEspessuraLapis(self):
        brush_size_dialog = JanelaEspessura()
        result = brush_size_dialog.exec_()

        if result == QDialog.Accepted:
            self.brush_size = brush_size_dialog.recebeEspessuraSelecionada()


    def retornarTextoImagem(self):
        global lista_de_letras

        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')

        retorna_classe = RetornaClasse()
        letra_digitalizada = retorna_classe.preverLetra(caminho_screenshot)
        self.minha_lista.append(letra_digitalizada)
        lista_de_letras = ''.join(str(valor) for valor in self.minha_lista if valor is not None and valor != 'e')
        self.tela_digitalizada.setPlainText(lista_de_letras)
        self.tela_digitalizada.setStyleSheet("font: 65pt 'Calibri'; background-color:#ffffff;")

    def mostrarLetraPontilhada(self):
        letras_dialog = JanelaLetraPontilhada()
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens', 'LetrasPontilhadas')
        result = letras_dialog.exec()
        if result == QDialog.Accepted:
            letra_selecionada = letras_dialog.letra_selecionada
            imagem_path = os.path.join(caminho_pasta_imagens, f"{letra_selecionada}.png")
            imagem_na_tela_label = QPixmap(imagem_path)
            print(f"Letra selecionada: {letra_selecionada}")
            self.setarImagem(imagem_na_tela_label)

    def apagarLetra(self):
        global lista_de_letras
        if len(lista_de_letras) == 0:
            mensagem = QMessageBox()
            mensagem.setIcon(QMessageBox.Information)
            mensagem.setText("Não há letras para serem apagadas!")
            mensagem.setWindowTitle("Alerta")
            mensagem.setStandardButtons(QMessageBox.Ok)

            mensagem.exec_()
        else:
            lista_de_letras = lista_de_letras[:-1]
            self.minha_lista.pop(-1)
            self.tela_digitalizada.setPlainText(lista_de_letras)
            self.tela_digitalizada.setStyleSheet("font: 65pt 'Calibri'; background-color:#ffffff;")

    def salvarDocumento(self):
        global lista_de_letras

        caminho_do_arquivo, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo TXT", "",
                                                            "Arquivos de Texto (*.txt);;Todos os Arquivos (*)")

        if caminho_do_arquivo:
            with open(caminho_do_arquivo, 'w') as arquivo_txt:
                for letra in lista_de_letras:
                    arquivo_txt.write(f"{letra}")

        mensagem = QMessageBox()
        mensagem.setText("Documento salvo com sucesso!")
        mensagem.setWindowTitle('Salvamento concluído')
        mensagem.setStandardButtons(QMessageBox.Ok)
        return mensagem.exec_()


    def perguntaSobreAbrirNovoDocumento(self):
        global lista_de_letras
        if len(lista_de_letras) == 0:
            mensagem = QMessageBox()
            mensagem.setText("O documento já está em branco")
            mensagem.setWindowTitle('Não há alterações no documento')
            mensagem.setStandardButtons(QMessageBox.Ok)
            return mensagem.exec_()
        else:
            mensagem = QMessageBox()
            mensagem.setWindowTitle('Salvar Alterações')
            mensagem.setText('Deseja salvar as alterações do documento atual?')
            mensagem.setStandardButtons(QMessageBox.Save | QMessageBox.No)
            return mensagem.exec_()


    def abrirNovoDocumento(self):
        global lista_de_letras
        resposta = self.perguntaSobreAbrirNovoDocumento()
        if resposta == QMessageBox.Ok:
            return
        if resposta == QMessageBox.Save:
            self.salvarDocumento()
            lista_de_letras = ""
            self.minha_lista.clear()
            self.tela_digitalizada.setPlainText(lista_de_letras)
            self.tela_digitalizada.setStyleSheet("font: 65pt 'Calibri'; background-color:#ffffff;")
        if resposta == QMessageBox.No:
            lista_de_letras = ""
            self.minha_lista.clear()
            self.tela_digitalizada.setPlainText(lista_de_letras)
            self.tela_digitalizada.setStyleSheet("font: 65pt 'Calibri'; background-color:#ffffff;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()