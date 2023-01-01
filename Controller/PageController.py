from Controller.ConnectionDBController import ConnectionDBController
from Controller.LoginController import LoginController
from Controller.CadastroController import CadastroController
from Controller.AdministradorController import AdministradorController


class PageController:
    def __init__(self) -> None:
        self.conn = ConnectionDBController.get_connection()
    
    def mostrar_tela_login(self):
        try:
            self.login = LoginController(self.conn)
            self.login.tela_cadastro.connect(self.mostrar_tela_cadastro)
            self.login.tela_administrador.connect(self.mostrar_tela_administrador)
            self.login.show()
            
        except Exception as ex:
            print(ex)
            
    def mostrar_tela_cadastro(self):
        try:
            self.login.close()
            self.cadastro = CadastroController(self.conn)
            self.cadastro.voltar_tela.connect(self.mostrar_tela_login)
            self.cadastro.show()
        except Exception as ex:
            print(ex)

    def mostrar_tela_administrador(self):
        try:
            self.login.close()
            self.administrador = AdministradorController(self.conn)
            self.administrador.voltar_tela.connect(self.mostrar_tela_login)
            self.administrador.show()
        except Exception as ex:
            print(ex)
