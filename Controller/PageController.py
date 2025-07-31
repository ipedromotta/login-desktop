from Content.Log import logger
from Controller.LoginController import LoginController
from Controller.CadastroController import CadastroController
from Controller.AdministradorController import AdministradorController


class PageController:
    def __init__(self):
        self.login = LoginController()
        self.cadastro = CadastroController()
        self.administrador = AdministradorController()

    def mostrar_tela_login(self):
        try:
            logger.debug(".mostrar_tela_login")
            self.login.ui.senha.clear()
            self.login.ui.usuario.clear()
            self.login.ui.lbl_erro.clear()
            self.login.ui.usuario.setFocus()
            self.login.tela_cadastro.connect(self.mostrar_tela_cadastro)
            self.login.tela_administrador.connect(self.mostrar_tela_administrador)
            self.login.show()
            
        except Exception as e:
            logger.error(f"Erro ao mostrar tela de login: {e}", exc_info=True)
            
    def mostrar_tela_cadastro(self):
        try:
            logger.debug(".mostrar_tela_cadastro")
            self.login.close()
            self.cadastro.voltar_tela.connect(self.mostrar_tela_login)
            self.cadastro.show()
        except Exception as e:
            logger.error(f"Erro ao mostrar tela de cadastro: {e}", exc_info=True)

    def mostrar_tela_administrador(self):
        try:
            logger.debug(".mostrar_tela_administrador")
            self.login.close()
            self.administrador.carregar_dados()
            self.administrador.voltar_tela.connect(self.mostrar_tela_login)
            self.administrador.show()
        except Exception as e:
            logger.error(f"Erro ao mostrar tela de administrador: {e}", exc_info=True)
