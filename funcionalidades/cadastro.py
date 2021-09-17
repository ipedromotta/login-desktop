from .database import banco

class Cadastro:
    
    def cadastrar(self):
        usuario = self.tela_cadastro.lineEdit.text()
        senha = self.tela_cadastro.lineEdit_2.text()

        if usuario == "" or senha == "":
            self.tela_cadastro.label_5.setText("Preencha todos os campos!")
            return

        self.tela_cadastro.label_4.setText("Usuário cadastrado com sucesso!")
        self.tela_cadastro.label_5.setText("")
        cursor = banco.cursor()
        query = "INSERT INTO dados (usuario, senha) VALUES (%s,%s)"
        info = (str(usuario), str(senha))
        cursor.execute(query, info)
        banco.commit()
        self.tela_cadastro.lineEdit.setText("")
        self.tela_cadastro.lineEdit_2.setText("")