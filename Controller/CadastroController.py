from PyQt5 import QtWidgets, QtCore

from Content.Log import logger
from View.Cadastro import Ui_Cadastro
from Model.UsuarioModel import UsuarioModel


class CadastroController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        self.iniciar_eventos()
        
    def iniciar_eventos(self):
        logger.info("Iniciando eventos da pagina - cadastro")
        self.ui.btn_cadastrar.clicked.connect(lambda: self.cadastrar(self.ui.nome.text(), self.ui.usuario.text(), self.ui.senha.text()))
        self.ui.btn_voltar.clicked.connect(self.voltar)
        
    def cadastrar(self, nome:str, usuario:str, senha:str) -> None:
        logger.info("Cadastrando usuario...")
        if usuario == "" or senha == "" or nome == "":
            self.ui.lbl_erro.setText("Preencha todos os campos!")
            return

        if UsuarioModel.usuario_existe(usuario):
            self.ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
            return

        cadastrou = UsuarioModel.cadastrar(nome, usuario, senha)

        # interface.limpar_cadastro.emit()

        if cadastrou:
            logger.info("Usuário cadastrado com sucesso!")
            self.ui.lbl_erro.setText("Usuário cadastrado com sucesso!")
            self.ui.nome.clear()
            self.ui.senha.clear()
            self.ui.usuario.clear()
        else:
            logger.info("Usuário não foi cadastrado")
            self.ui.lbl_erro.setText("Usuário não foi cadastrado")
            
    def voltar(self):
        self.close()
        self.ui.nome.clear()
        self.ui.senha.clear()
        self.ui.usuario.clear()
        self.ui.lbl_erro.clear()
        self.voltar_tela.emit()
