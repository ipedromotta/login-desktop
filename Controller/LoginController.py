from PyQt5 import QtWidgets, QtCore

from Content.Log import logger
from View.Login import Ui_Login
from View.Logado import Ui_Logado
from Model.UsuarioModel import UsuarioModel



class LoginController(QtWidgets.QMainWindow):
    tela_cadastro = QtCore.pyqtSignal()
    tela_administrador = QtCore.pyqtSignal()
      
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Login()
        self.iniciar_eventos()

    def iniciar_eventos(self) -> None:
        logger.info("Iniciando eventos da pagina de login")
        self.ui.setupUi(self)
        self.ui.btn_entrar.clicked.connect(lambda: self.logar(self.ui.usuario.text(), self.ui.senha.text()))
        self.ui.btn_cadastrar.clicked.connect(self.tela_cadastro.emit)
    
    def logar(self, usuario:str, senha:str) -> None:
        logger.info("Logando...")
        if usuario == "" or senha == "":
            logger.warning("Tentativa de login com campos vazios")
            self.ui.lbl_erro.setText("Preencha todos os campos!")
            return

        usuario = UsuarioModel.logar(usuario, senha)

        if not usuario:
            logger.warning("Login ou senha incorreto!")
            self.ui.lbl_erro.setText("Login ou senha incorreto!")
            return

        if usuario.administrador:
            logger.info("Logado com sucesso! administrador")
            self.tela_administrador.emit()
        else:
            logger.info("Logado com sucesso!")
            self.mostrar_tela_logado(usuario)

    def mostrar_tela_logado(self, usuario:UsuarioModel) -> None:
        try:
            self.ui_logado = Ui_Logado()
            self.ui_logado.setupUi(self)
            self.ui_logado.lbl_nome.setText(f"Olá, {usuario.nome}!")
            self.ui_logado.btn_logout.clicked.connect(self.iniciar_eventos)
        except Exception as e:
            logger.error(f"Erro ao mostrar tela de logado - {e}", exc_info=True)
