from PyQt5 import QtWidgets
from funcionalidades import Telas, Cadastro, Edicao, Exclusao, Armazenamento, Acesso


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    telas = Telas()
    telas.tela_cadastro.pushButton.clicked.connect(lambda: Cadastro.cadastrar(telas))
    telas.tela_cadastro.pushButton_2.clicked.connect(lambda: Acesso.sair(telas))
    telas.tela_principal.pushButton_2.clicked.connect(lambda: Acesso.inicio(telas))
    telas.tela_principal.pushButton.clicked.connect(lambda: Acesso.login(telas))
    telas.tela_logado.pushButton.clicked.connect(lambda: Acesso.logout(telas))
    telas.tela_admin.pushButton.clicked.connect(lambda: Acesso.logout(telas))
    telas.tela_admin.pushButton_2.clicked.connect(lambda: Exclusao.ExcluirDados(telas))
    telas.tela_admin.pushButton_3.clicked.connect(lambda: Edicao.EditarDados(telas))

    telas.tela_editar.pushButton.clicked.connect(lambda: Acesso.logout_editar(telas))
    telas.tela_editar.pushButton_2.clicked.connect(lambda: Armazenamento.SalvarEdicao(telas))
    telas.tela_principal.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
    telas.tela_cadastro.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

    telas.tela_principal.show()
    app.exec()
