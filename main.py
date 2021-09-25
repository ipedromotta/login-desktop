from PyQt5 import QtWidgets
from funcionalidades import Telas, Cadastro, Edicao, Exclusao, Armazenamento, Acesso


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    telas = Telas()
    telas.tela_cadastro.btn_cadastrar.clicked.connect(lambda: Cadastro.cadastrar(telas))
    telas.tela_cadastro.btn_voltar.clicked.connect(lambda: Acesso.logout_cadastro(telas))
    telas.tela_principal.btn_cadastrar.clicked.connect(telas.tela_cadastrar)
    telas.tela_principal.btn_entrar.clicked.connect(lambda: Acesso.login(telas))
    telas.tela_logado.btn_logout.clicked.connect(lambda: Acesso.logout_logado(telas))
    telas.tela_admin.btn_logout.clicked.connect(lambda: Acesso.logout_admin(telas))
    telas.tela_admin.btn_excluir.clicked.connect(lambda: Exclusao.excluir_dados(telas))
    telas.tela_admin.btn_editar.clicked.connect(lambda: Edicao.editar_dados(telas))

    telas.tela_editar.btn_cancelar.clicked.connect(lambda: Acesso.logout_editar(telas))
    telas.tela_editar.btn_salvar.clicked.connect(lambda: Armazenamento.salvar_edicao(telas))
    telas.tela_principal.senha.setEchoMode(QtWidgets.QLineEdit.Password)
    telas.tela_cadastro.senha.setEchoMode(QtWidgets.QLineEdit.Password)

    telas.tela_principal.show()
    app.exec()
