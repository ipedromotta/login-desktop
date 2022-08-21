from Model.UsuarioModel import UsuarioModel


class LoginController:
    def login(self, interface, usuario:str, senha:str, conn) -> None:
        if usuario == "" or senha == "":
            interface.msg.emit("Preencha todos os campos!")
            return

        usuario = UsuarioModel().logar(usuario, senha, conn)

        if not usuario:
            interface.msg.emit("Login ou senha incorreto!")
            return

        if usuario.Administrador:
            interface.admin()
        else:
            interface.logar(usuario)
