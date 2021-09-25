from PyQt5 import uic, QtWidgets
from .database import banco

class Telas:

    def __init__(self):
        self.tela_cadastro = uic.loadUi("./interfaces/tela_cadastro.ui")
        self.tela_principal = uic.loadUi("./interfaces/tela_principal.ui")
        self.tela_logado = uic.loadUi("./interfaces/tela_logado.ui")
        self.tela_admin = uic.loadUi("./interfaces/tela_admin.ui")
        self.tela_editar = uic.loadUi("./interfaces/tela_editar.ui")

    def tela_adm(self):
        self.tela_admin.show()
        cursor = banco.cursor()
        query = "SELECT * FROM dados"
        cursor.execute(query)
        dados_lidos = cursor.fetchall()

        self.tela_admin.tbl_usuarios.setRowCount(len(dados_lidos))
        self.tela_admin.tbl_usuarios.setColumnCount(3)

        for linha in range(0, len(dados_lidos)):
            for coluna in range(0, 3):
                self.tela_admin.tbl_usuarios.setItem(
                    linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))
    
    def tela_cadastrar(self):
        self.tela_principal.close()
        self.tela_cadastro.show()
