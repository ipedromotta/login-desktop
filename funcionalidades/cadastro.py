from .database import banco

class Cadastro:
    
    def cadastrar(self):
        usuario = self.tela_cadastro.usuario.text()
        senha = self.tela_cadastro.senha.text()

        if usuario == "" or senha == "":
            self.tela_cadastro.lbl_erro.setText("Preencha todos os campos!")
            return

        self.tela_cadastro.lbl_msg.setText("Usuário cadastrado com sucesso!")
        self.tela_cadastro.lbl_erro.setText("")
        
        cursor = banco.cursor()
        query = "INSERT INTO dados (usuario, senha) VALUES (%s,%s)"
        info = (str(usuario), str(senha))
        cursor.execute(query, info)
        banco.commit()

        self.tela_cadastro.usuario.setText("")
        self.tela_cadastro.senha.setText("")
