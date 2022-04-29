from PyQt5 import QtWidgets

from Controller.AcoesController import AcoesController
from Controller.ConectionDBController import ConectionDBController
from View.tela_admin import Ui_Admin
from View.tela_cadastro import Ui_TelaCadastro
from View.tela_editar import Ui_TelaEdicao
from View.tela_logado import Ui_TelaLogado
from View.tela_principal import Ui_MainWindow

cnxn = ConectionDBController.get_connection()

acoes = AcoesController()

tela_logado = Ui_TelaLogado()
tela_principal = Ui_MainWindow()
tela_cadastro = Ui_TelaCadastro()
tela_admin = Ui_Admin()
tela_edicao = Ui_TelaEdicao()

class AcessoController:
    def login(self, ui, tela, usuario, senha):

        if usuario == "" or senha == "":
            ui.lbl_erro.setText("Preencha todos os campos!")
            return

        cursor = cnxn.cursor(dictionary=True)
        query = f"SELECT * FROM dados WHERE usuario ='{usuario}' and senha = '{senha}'"
        cursor.execute(query)
        resultado = cursor.fetchone()

        if resultado == None:
            ui.lbl_erro.setText("Login ou senha incorreto!")
            return

        tela.close()
        if resultado['bl_adm'] == True:
            self.tela_adm(tela)
        else:
            tela_logado.setupUi(tela)
            tela_logado.btn_logout.clicked.connect(lambda: self.logout(tela))
            tela.show()

    def logout(self, tela):
        tela.close()
        tela_principal.setupUi(tela)
        tela_principal.btn_entrar.clicked.connect(lambda: self.login(tela_principal, tela, tela_principal.usuario.text(), tela_principal.senha.text()))
        tela_principal.btn_cadastrar.clicked.connect(lambda: self.tela_de_cadastro(tela))
        tela.show()

    def tela_de_cadastro(self, tela):
        tela.close()
        tela_cadastro.setupUi(tela)
        tela_cadastro.btn_cadastrar.clicked.connect(lambda: acoes.cadastrar(cnxn, tela_cadastro, tela_cadastro.usuario.text(), tela_cadastro.senha.text()))
        tela_cadastro.btn_voltar.clicked.connect(lambda: self.logout(tela))
        tela.show()

    def tela_adm(self, tela):
        tela.close()
        tela_admin.setupUi(tela)
        tela_admin.btn_logout.clicked.connect(lambda: self.logout(tela))

        cursor = cnxn.cursor()
        query = "SELECT * FROM dados"
        cursor.execute(query)
        dados_lidos = cursor.fetchall()

        tela_admin.tbl_usuarios.setRowCount(len(dados_lidos))
        tela_admin.tbl_usuarios.setColumnCount(3)

        for linha in range(0, len(dados_lidos)):
            for coluna in range(0, 3):
                tela_admin.tbl_usuarios.setItem(
                    linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))

        tela_admin.btn_editar.clicked.connect(lambda: acoes.editar_dados(cnxn, tela_edicao, tela_admin, tela, self.tela_adm))
        tela_admin.btn_excluir.clicked.connect(lambda: acoes.excluir_dados(cnxn, tela_admin))

        tela.show()
