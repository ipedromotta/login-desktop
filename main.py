import sys
from PyQt5 import QtWidgets
from View.tela_principal import Ui_MainWindow
from Controller.AcessoController import AcessoController

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    tela = QtWidgets.QMainWindow()
    acesso = AcessoController()

    ui = Ui_MainWindow()
    ui.setupUi(tela)

    ui.btn_entrar.clicked.connect(lambda: acesso.login(ui, tela, ui.usuario.text(), ui.senha.text()))
    ui.btn_cadastrar.clicked.connect(lambda: acesso.tela_de_cadastro(tela))
    
    tela.show()
    sys.exit(app.exec_())
