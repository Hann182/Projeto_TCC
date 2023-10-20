import typing
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import os, sys

sys.path.insert(1, './view')

from View.Cadastro import *
from Repositories.banco.Query import Sqlite_DB

class Cadastro(QDialog):
    def __init__(self, *args, **argvs):
        super(Cadastro,self).__init__(*args, **argvs)
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)
        self.ui.btnConfirma.clicked.connect(self.add)
        self.ui.btnLimpar.clicked.connect(self.limpa)

    def add(self):
        db = Sqlite_DB("./repositories/usuarios_cadastrados.db")
       
        name = self.ui.imName.text()
        passd = self.ui.imPass.text()
        passc = self.ui.imPassC.text()

        if name=='' or passc == '' or passd == '':
            QMessageBox.warning(QMessageBox(), 'Alerta!','Campo(s) vazio(s)')
        elif passc != passd:
            QMessageBox.warning(QMessageBox(), 'Alerta!','Senhas divergentes')
        else:
            db.crud("INSERT INTO usuarios (nome, senha) VALUES('{}', '{}')".format(name, passd))
            QMessageBox.information(QMessageBox(), 'Cadastro', 'Cadastro realizada')

    def limpa(self):
        self.ui.imName.setText('')
        self.ui.imPass.setText('')
        self.ui.imPassC.setText('')

    