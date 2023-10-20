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

from View.TelaLogin import *
from Cadastrar import Cadastro
from Repositories.Banco.Query import Sqlite_DB
from View.TelaInterativa import Window

class Login(QDialog):
    def __init__(self, *args, **argvs):
        super(Login, self).__init__(*args, **argvs)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.ui.btnEntrar.clicked.connect(self.login)
        self.ui.btnCadasto.clicked.connect(self.cadastro)
        self.ui.btnApagar.clicked.connect(self.limpar)
        
    def login(self):
        db = Sqlite_DB("usuarios_cadastrados.db")

        user = self.ui.imName.text()
        passd = self.ui.ImPassword.text()
        if user == '' or passd == '':
            QMessageBox.warning(QMessageBox(), 'Alerta!','Campo(s) vazio(s), por favor preencha!')
        else:
            dados = db.dados("SELECT * from usuarios WHERE nome = '{}' and senha = '{}'".format(user, passd))
            if dados:
                QMessageBox.information(QMessageBox(), 'Login Realizado', 'Bem vindo ' + user)
                self.window = Window()
                self.window.show()
                self.hide()
            else:
                QMessageBox.information(QMessageBox(), 'Login invalido', 'Senha ou usuario incorreto')

    def limpar(self):
        self.ui.imName.clear()
        self.ui.ImPassword.clear()

    def cadastro(self):
        self.window = Cadastro()
        self.window.show()

app = QApplication(sys.argv)
if (QDialog.Accepted == True):
    window = Login()
    window.show()
sys.exit(app.exec_())