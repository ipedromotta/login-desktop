from PyQt5 import QtWidgets, QtCore

from Model.UsuarioModel import UsuarioModel

from View.Login import Ui_Login
from View.Logado import Ui_Logado


class LoginController(QtWidgets.QMainWindow):
    tela_cadastro = QtCore.pyqtSignal()
    tela_administrador = QtCore.pyqtSignal()
      
    def __init__(self, conn=None) -> None:
        super().__init__()
        self.ui = Ui_Login()
        self.iniciar_eventos()
        self._conn = conn
        
    def iniciar_eventos(self):
        self.ui.setupUi(self)
        self.ui.btn_entrar.clicked.connect(lambda: self.logar(self.ui.usuario.text(), self.ui.senha.text(), self._conn))
        self.ui.btn_cadastrar.clicked.connect(self.tela_cadastro.emit)
    
    def logar(self, usuario:str, senha:str, conn) -> None:
        if usuario == "" or senha == "":
            self.ui.lbl_erro.setText("Preencha todos os campos!")
            return

        usuario = UsuarioModel().logar(usuario, senha, conn)

        if not usuario:
            self.ui.lbl_erro.setText("Login ou senha incorreto!")
            return

        if usuario.Administrador:
            self.tela_administrador.emit()
        else:
            self.mostrar_tela_logado(usuario)

    def mostrar_tela_logado(self, usuario:object) -> None:
        try:
            self.ui_logado = Ui_Logado()
            self.ui_logado.setupUi(self)
            self.ui_logado.lbl_nome.setText(f"Olá, {usuario.Nome}!")
            self.ui_logado.btn_logout.clicked.connect(self.iniciar_eventos)
        except Exception as ex:
            print(ex)
