import sys, os, signal
from PyQt5 import QtWidgets

from Controller.PageController import PageController


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)

        controller = PageController()
        controller.mostrar_tela_login()

        if not app.exec_():
            try:
                os.kill(os.getpid(), signal.SIGINT)
                sys.exit(0)
            except Exception as ex:
                print(ex)
                
    except Exception as ex:
        app.closeAllWindows()
        app.quit()
        os.kill(os.getpid(), signal.SIGINT)
        print(ex)
        sys.exit(0)
