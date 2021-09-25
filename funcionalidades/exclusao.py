from .database import banco

class Exclusao:
    
    def excluir_dados(self):
        linha = self.tela_admin.tbl_usuarios.currentRow()
        self.tela_admin.tbl_usuarios.removeRow(linha)

        cursor = banco.cursor()
        cursor.execute("SELECT id FROM dados")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM dados WHERE id =" + str(valor_id))
        banco.commit()
