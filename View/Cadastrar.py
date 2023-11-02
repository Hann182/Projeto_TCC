import os

from View.TelaCadastro import *
from Repositories.Banco.CriarBanco import sqlite_db

class Cadastro(QDialog):

    def __init__(self, *args, **argvs):
        super(Cadastro,self).__init__(*args, **argvs)
        self.ui = Ui_cadastro()
        self.ui.setupUi(self)
        self.ui.btnConfirma.clicked.connect(self.add)
        self.ui.btnLimpar.clicked.connect(self.limpa)

    def add(self):
        caminho_pasta_banco = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Repositories', 'Banco')
        db = sqlite_db(os.path.join(caminho_pasta_banco, 'banco.db'))
       
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

    