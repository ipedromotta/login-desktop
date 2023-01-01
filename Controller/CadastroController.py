from PyQt5 import QtWidgets, QtCore

from View.Cadastro import Ui_Cadastro
from Model.UsuarioModel import UsuarioModel


class CadastroController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self, conn=None) -> None:
        super().__init__()
        self.ui = Ui_Cadastro()
        self._conn = conn
        self.ui.setupUi(self)
        self.iniciar_eventos()
        
    def iniciar_eventos(self):
        self.ui.btn_cadastrar.clicked.connect(lambda: self.cadastrar(self.ui.nome.text(), self.ui.usuario.text(), self.ui.senha.text()))
        self.ui.btn_voltar.clicked.connect(self.voltar)
        
    def cadastrar(self, nome:str, usuario:str, senha:str) -> None:
        if usuario == "" or senha == "" or nome == "":
            self.ui.lbl_erro.setText("Preencha todos os campos!")
            return

        usuario_existe = UsuarioModel.usuario_existe(usuario, self._conn)
        if usuario_existe:
            self.ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
            return

        cadastrou = UsuarioModel.cadastrar(nome, usuario, senha, self._conn)

        # interface.limpar_cadastro.emit()

        if cadastrou:
            self.ui.lbl_erro.setText("Usuário cadastrado com sucesso!")
        else:
            self.ui.lbl_erro.setText("Usuário não foi cadastrado")
            
    def voltar(self):
        self.close()
        self.voltar_tela.emit()
