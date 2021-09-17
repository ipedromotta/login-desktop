from .database import banco

class Edicao:

    def EditarDados(self):
        self.tela_editar.show()
        linha = self.tela_admin.tableWidget.currentRow()

        cursor = banco.cursor()
        cursor.execute("SELECT id FROM dados")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM dados WHERE id =" + str(valor_id))
        usuario = cursor.fetchall()
        self.numero_id = valor_id

        self.tela_editar.lineEdit.setText(str(usuario[0][1]))
        self.tela_editar.lineEdit_2.setText(str(usuario[0][2]))