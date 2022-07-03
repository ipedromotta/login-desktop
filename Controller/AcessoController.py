from PyQt5 import QtWidgets, QtCore

from Controller.AcoesController import AcoesController
from Controller.ConnectionDBController import ConnectionDBController

from Model.UsuarioModel import UsuarioModel
from Model.AdminModel import AdminModel

from View.tela_admin import Ui_Admin
from View.tela_cadastro import Ui_TelaCadastro
from View.tela_editar import Ui_TelaEdicao
from View.tela_logado import Ui_TelaLogado
from View.tela_principal import Ui_MainWindow


class AcessoController:
    def __init__(self) -> None:
        self.__cnxn = ConnectionDBController.get_connection()
        self.__acoes = AcoesController()
        self.__tela_logado = Ui_TelaLogado()
        self.__tela_principal = Ui_MainWindow()
        self.__tela_cadastro = Ui_TelaCadastro()
        self.__tela_admin = Ui_Admin()
        self.__tela_edicao = Ui_TelaEdicao()
        

    def login(self, ui, tela, usuario, senha):

        if usuario == "" or senha == "":
            ui.lbl_erro.setText("Preencha todos os campos!")
            return

        usuario = UsuarioModel().logar(usuario, senha, self.__cnxn)

        if not usuario:
            ui.lbl_erro.setText("Login ou senha incorreto!")
            return

        tela.close()
        if usuario.Administrador:
            self.tela_adm(tela)
        else:
            self.__tela_logado.setupUi(tela)
            self.__tela_logado.btn_logout.clicked.connect(lambda: self.logout(tela))
            self.__tela_logado.lbl_nome.setText(f"Olá, {usuario.Nome}!")
            tela.show()

    def logout(self, tela):
        tela.close()
        self.__tela_principal.setupUi(tela)
        self.__tela_principal.btn_entrar.clicked.connect(lambda: self.login(self.__tela_principal, tela, self.__tela_principal.usuario.text(), self.__tela_principal.senha.text()))
        self.__tela_principal.btn_cadastrar.clicked.connect(lambda: self.tela_de_cadastro(tela))
        tela.show()

    def tela_de_cadastro(self, tela):
        tela.close()
        self.__tela_cadastro.setupUi(tela)
        self.__tela_cadastro.btn_cadastrar.clicked.connect(lambda: self.__acoes.cadastrar(self.__cnxn, self.__tela_cadastro, self.__tela_cadastro.nome.text(), self.__tela_cadastro.usuario.text(), self.__tela_cadastro.senha.text()))
        self.__tela_cadastro.btn_voltar.clicked.connect(lambda: self.logout(tela))
        tela.show()

    def tela_adm(self, tela):
        tela.close()
        self.__tela_admin.setupUi(tela)
        self.__tela_admin.btn_logout.clicked.connect(lambda: self.logout(tela))

        dados_lidos = AdminModel.consultar_usuarios(self.__cnxn)

        self.__tela_admin.tbl_usuarios.setRowCount(len(dados_lidos))
        self.__tela_admin.tbl_usuarios.setColumnCount(3)

        for linha in range(0, len(dados_lidos)):
            for coluna in range(0, 3):
                item = QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna]))
                item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                self.__tela_admin.tbl_usuarios.setItem(linha, coluna, item)

        self.__tela_admin.btn_editar.clicked.connect(lambda: self.__acoes.editar_dados(self.__cnxn, self.__tela_edicao, self.__tela_admin, tela, self.tela_adm))
        self.__tela_admin.btn_excluir.clicked.connect(lambda: self.__acoes.excluir_dados(self.__cnxn, self.__tela_admin))

        tela.show()
