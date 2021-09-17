from .database import banco
from .telas import Telas

class Acesso:

    def login(self):
        self.tela_principal.label_3.setText("")
        nome_usuario = self.tela_principal.lineEdit.text()
        senha = self.tela_principal.lineEdit_2.text()
        cursor = banco.cursor()
        query = "SELECT usuario, senha FROM dados WHERE usuario like'" + \
            nome_usuario+"' and senha like '" + senha + "'"
        cursor.execute(query)
        resultado = cursor.fetchone()

        if resultado == None:
            self.tela_principal.label_3.setText("Login ou senha incorreto!")
        elif nome_usuario == "admin" and senha == "admin":
            self.tela_principal.lineEdit.setText("")
            self.tela_principal.lineEdit_2.setText("")
            self.tela_principal.close()
            self.tela_admin.show()
            Telas.TelaAdmin(self)

        else:
            self.tela_principal.lineEdit.setText("")
            self.tela_principal.lineEdit_2.setText("")
            self.tela_principal.close()
            self.tela_logado.show()

    def inicio(self):
        self.tela_principal.close()
        self.tela_cadastro.show()

    def logout(self):
        self.tela_logado.close()
        self.tela_admin.close()
        self.tela_principal.show()

    def logout_editar(self):
        self.tela_editar.close()
        self.tela_editar.lineEdit.setText("")
        self.tela_editar.lineEdit_2.setText("")

    def sair(self):
        self.tela_cadastro.label_4.setText("")
        self.tela_cadastro.label_5.setText("")
        self.tela_cadastro.close()
        self.tela_principal.show()


