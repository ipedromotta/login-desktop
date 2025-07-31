import sys
import argparse

from PyQt5 import QtWidgets

from Content.Log import logger
from Model.UsuarioModel import UsuarioModel
from Controller.PageController import PageController


__version__ = "2.0.0"


def configurar_argumentos():
    parser = argparse.ArgumentParser(description="Aplicação de Gerenciamento de Usuários")
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")
    return parser.parse_args()


def iniciar_aplicacao():
    logger.info(f"Iniciando aplicação - versão {__version__}")
    app = QtWidgets.QApplication(sys.argv)

    try:
        UsuarioModel.verificar_admin()

        controller = PageController()
        controller.mostrar_tela_login()

        logger.info("Aplicação iniciada com sucesso")
        sys.exit(app.exec_())

    except Exception as e:
        logger.critical(f"Erro crítico na aplicação: {e}", exc_info=True)
        app.closeAllWindows()
        app.quit()
        sys.exit(1)


if __name__ == "__main__":
    configurar_argumentos()
    iniciar_aplicacao()
