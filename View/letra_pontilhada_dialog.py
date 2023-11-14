import sys
from PyQt5.QtWidgets import QPushButton, QDialog, QGridLayout
from PyQt5.QtGui import QPixmap


class LetraPontilhadaDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecione uma letra")
        self.setFixedSize(300, 200)
        self.letra_selecionada = None  # Variável para armazenar a letra selecionada

        layout = QGridLayout()
        row, col = 0, 0

        for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            button = QPushButton(letra, self)
            button.setMaximumWidth(30)
            button.setMaximumHeight(30)
            button.clicked.connect(lambda _, letra=letra: self.set_letra_selecionada(letra))
            layout.addWidget(button, row, col)
            col += 1

            if col > 6:
                col = 0
                row += 1

        self.setLayout(layout)

    def set_letra_selecionada(self, letra):
        self.letra_selecionada = letra
        self.accept()