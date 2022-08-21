from PyQt5 import QtCore, QtWidgets

from Controller.LoginController import LoginController
from Controller.AcoesController import AcoesController

from View.Login import Ui_Login
from View.Logado import Ui_Logado
from View.Cadastro import Ui_Cadastro
from View.Admin import Ui_Admin
from View.Edicao import Ui_Edicao


class InterfaceLogin(QtCore.QObject):
    msg = QtCore.pyqtSignal(str)
    msg_cadastro = QtCore.pyqtSignal(str)
    limpar_cadastro = QtCore.pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Login()
        self.ui_logado = Ui_Logado()
        self.ui_cadastro = Ui_Cadastro()
        self.ui_admin = Ui_Admin()
        self.ui_edicao = Ui_Edicao()
        self.acesso = LoginController()
        self.acoes = AcoesController()
        self.msg.connect(self.inserir_mensagem)
        self.msg_cadastro.connect(self.inserir_mensagem_cadastro)
        self.limpar_cadastro.connect(self.reset_cadastro)
                
    def show(self) -> None:
        self.ui.setupUi(self.window)
        self.ui.btn_entrar.clicked.connect(lambda: self.acesso.login(self, self.ui.usuario.text(), self.ui.senha.text(), self.acoes.cnxn))
        self.ui.btn_cadastrar.clicked.connect(self.cadastrar)
        
        if not self.window.isActiveWindow():
            self.window.show()
        
    def logar(self, usuario:object) -> None:
        self.ui_logado.setupUi(self.window)
        self.ui_logado.lbl_nome.setText(f"Olá, {usuario.Nome}!")
        self.ui_logado.btn_logout.clicked.connect(self.show)
        
    def cadastrar(self) -> None:
        self.ui_cadastro.setupUi(self.window)
        self.ui_cadastro.btn_cadastrar.clicked.connect(lambda: self.acoes.cadastrar(self, self.ui_cadastro.nome.text(), self.ui_cadastro.usuario.text(), self.ui_cadastro.senha.text()))
        self.ui_cadastro.btn_voltar.clicked.connect(self.show)
        
    def admin(self) -> None:
        self.ui_admin.setupUi(self.window)
        self.ui_admin.btn_logout.clicked.connect(self.show)
        dados_lidos = self.acoes.consultar_cadastros()
        
        self.ui_admin.tbl_usuarios.setRowCount(len(dados_lidos))
        self.ui_admin.tbl_usuarios.setColumnCount(3)
        for linha in range(0, len(dados_lidos)):
            for coluna in range(0, 3):
                item = QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.ui_admin.tbl_usuarios.setItem(linha, coluna, item)
                
        self.ui_admin.btn_editar.clicked.connect(lambda: self.editar_dados(dados_lidos))
        self.ui_admin.btn_excluir.clicked.connect(lambda: self.excluir_usuario(dados_lidos))
        
    def editar_dados(self, dados_lidos:dict) -> None:
        usuario_selecionado = self.ui_admin.tbl_usuarios.currentRow()
        self.ui_edicao.setupUi(self.window)
        self.ui_edicao.btn_cancelar.clicked.connect(self.admin)
        
        self.acoes.editar_dados(dados_lidos, usuario_selecionado, self.ui_edicao, self.admin)
        
    def excluir_usuario(self, dados_lidos:dict) -> None:
        usuario_selecionado = self.ui_admin.tbl_usuarios.currentRow()
        self.ui_admin.tbl_usuarios.removeRow(usuario_selecionado)
        
        self.acoes.excluir_dados(dados_lidos, usuario_selecionado)
        
        
    @QtCore.pyqtSlot(str)
    def inserir_mensagem(self, msg:str) -> None:        
        self.ui.lbl_erro.setText(msg)
        
    @QtCore.pyqtSlot(str)
    def inserir_mensagem_cadastro(self, msg:str) -> None:
        self.ui_cadastro.lbl_erro.setText(msg)
        
    @QtCore.pyqtSlot()
    def reset_cadastro(self) -> None:
        self.ui_cadastro.lbl_erro.setText("")
        self.ui_cadastro.nome.setText("")
        self.ui_cadastro.usuario.setText("")
        self.ui_cadastro.senha.setText("")