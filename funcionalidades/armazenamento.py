from .database import banco
from .telas import Telas

class Armazenamento:

    def SalvarEdicao(self):
        usuario = self.tela_editar.lineEdit.text()
        senha = self.tela_editar.lineEdit_2.text()

        cursor = banco.cursor()
        cursor.execute("UPDATE dados SET usuario = '{}', senha = '{}' WHERE id = {}".format(
            usuario, senha, self.numero_id))
        banco.commit()

        self.tela_editar.close()
        self.tela_admin.close()
        Telas.TelaAdmin(self)