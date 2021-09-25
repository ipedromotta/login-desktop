from .database import banco

class Armazenamento:

    def salvar_edicao(self):
        usuario = self.tela_editar.novo_usuario.text()
        senha = self.tela_editar.nova_senha.text()

        cursor = banco.cursor()
        cursor.execute("UPDATE dados SET usuario = '{}', senha = '{}' WHERE id = {}".format(
                        usuario, senha, self.numero_id))
        banco.commit()

        self.tela_editar.close()
        self.tela_admin.close()
        self.tela_adm()
