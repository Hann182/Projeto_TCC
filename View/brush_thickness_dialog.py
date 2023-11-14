import cv2, sys, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class BrushThicknessDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolher Espessura do Pincel")
        self.setFixedSize(200, 150)

        layout = QVBoxLayout()
        self.brush_size = 2
        options = ["Fina (10px)", "Média (20px)", "Grossa (30px)"]
        self.radio_buttons = []

        for option in options:
            radio_button = QRadioButton(option, self)
            layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)

        button = QPushButton("OK", self)
        button.clicked.connect(self.accept)

        layout.addWidget(button)
        self.setLayout(layout)

    def get_selected_thickness(self):
        for index, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                return [10, 20, 30][index]