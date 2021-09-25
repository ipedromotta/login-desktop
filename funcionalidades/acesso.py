from .database import banco

class Acesso:

    def login(self):
        self.tela_principal.lbl_erro.setText("")
        nome_usuario = self.tela_principal.usuario.text()
        senha = self.tela_principal.senha.text()
        cursor = banco.cursor()
        query = "SELECT usuario, senha FROM dados WHERE usuario like'" + \
                nome_usuario+"' and senha like '" + senha + "'"
        cursor.execute(query)
        resultado = cursor.fetchone()

        if resultado == None:
            self.tela_principal.lbl_erro.setText("Login ou senha incorreto!")
        elif nome_usuario == "admin" and senha == "admin":
            self.tela_principal.usuario.setText("")
            self.tela_principal.senha.setText("")
            self.tela_principal.close()
            self.tela_admin.show()
            self.tela_adm()

        else:
            self.tela_principal.usuario.setText("")
            self.tela_principal.senha.setText("")
            self.tela_principal.close()
            self.tela_logado.show()

    def logout_admin(self):
        self.tela_admin.close()
        self.tela_principal.show()

    def logout_logado(self):
        self.tela_logado.close()
        self.tela_principal.show()

    def logout_editar(self):
        self.tela_editar.close()
        self.tela_editar.novo_usuario.setText("")
        self.tela_editar.nova_senha.setText("")

    def logout_cadastro(self):
        self.tela_cadastro.lbl_msg.setText("")
        self.tela_cadastro.lbl_erro.setText("")
        self.tela_cadastro.close()
        self.tela_principal.show()
