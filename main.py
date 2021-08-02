from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuarios"
)


def excluir_dados():
    linha = tela_admin.tableWidget.currentRow()
    tela_admin.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM dados WHERE id =" + str(valor_id))
    banco.commit()


def editar_dados():
    global numero_id
    tela_editar.show()
    linha = tela_admin.tableWidget.currentRow()

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM dados WHERE id =" + str(valor_id))
    usuario = cursor.fetchall()
    numero_id = valor_id

    tela_editar.lineEdit.setText(str(usuario[0][1]))
    tela_editar.lineEdit_2.setText(str(usuario[0][2]))


def salvar_edicao():
    global numero_id
    usuario = tela_editar.lineEdit.text()
    senha = tela_editar.lineEdit_2.text()

    cursor = banco.cursor()
    cursor.execute("UPDATE dados SET usuario = '{}', senha = '{}' WHERE id = {}".format(
        usuario, senha, numero_id))
    banco.commit()

    tela_editar.close()
    tela_admin.close()
    admin()


def logout_editar():
    tela_editar.close()
    tela_editar.lineEdit.setText("")
    tela_editar.lineEdit_2.setText("")


def cadastrar():
    usuario = tela_cadastro.lineEdit.text()
    senha = tela_cadastro.lineEdit_2.text()

    if usuario == "" or senha == "":
        tela_cadastro.label_5.setText("Preencha todos os campos!")
        return

    tela_cadastro.label_4.setText("Usuário cadastrado com sucesso!")
    tela_cadastro.label_5.setText("")
    cursor = banco.cursor()
    query = "INSERT INTO dados (usuario, senha) VALUES (%s,%s)"
    info = (str(usuario), str(senha))
    cursor.execute(query, info)
    banco.commit()
    tela_cadastro.lineEdit.setText("")
    tela_cadastro.lineEdit_2.setText("")


def sair():
    tela_cadastro.label_4.setText("")
    tela_cadastro.label_5.setText("")
    tela_cadastro.close()
    tela_principal.show()


def inicio():
    tela_principal.close()
    tela_cadastro.show()


def login():
    tela_principal.label_3.setText("")
    nome_usuario = tela_principal.lineEdit.text()
    senha = tela_principal.lineEdit_2.text()
    cursor = banco.cursor()
    query = "SELECT usuario, senha FROM dados WHERE usuario like'" + \
        nome_usuario+"' and senha like '" + senha + "'"
    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado == None:
        tela_principal.label_3.setText("Login ou senha incorreto!")
    elif nome_usuario == "admin" and senha == "admin":
        tela_principal.lineEdit.setText("")
        tela_principal.lineEdit_2.setText("")
        tela_principal.close()
        tela_admin.show()
        admin()

    else:
        tela_principal.lineEdit.setText("")
        tela_principal.lineEdit_2.setText("")
        tela_principal.close()
        tela_logado.show()


def admin():
    tela_admin.show()
    cursor = banco.cursor()
    query = "SELECT * FROM dados"
    cursor.execute(query)
    dados_lidos = cursor.fetchall()

    tela_admin.tableWidget.setRowCount(len(dados_lidos))
    tela_admin.tableWidget.setColumnCount(3)

    for linha in range(0, len(dados_lidos)):
        for coluna in range(0, 3):
            tela_admin.tableWidget.setItem(
                linha, coluna, QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna])))


def logout():
    tela_logado.close()
    tela_admin.close()
    tela_principal.show()


app = QtWidgets.QApplication([])
tela_cadastro = uic.loadUi("./interfaces/tela_cadastro.ui")
tela_principal = uic.loadUi("./interfaces/tela_principal.ui")
tela_logado = uic.loadUi("./interfaces/tela_logado.ui")
tela_admin = uic.loadUi("./interfaces/tela_admin.ui")
tela_editar = uic.loadUi("./interfaces/tela_editar.ui")
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_2.clicked.connect(sair)
tela_principal.pushButton_2.clicked.connect(inicio)
tela_principal.pushButton.clicked.connect(login)
tela_logado.pushButton.clicked.connect(logout)
tela_admin.pushButton.clicked.connect(logout)
tela_admin.pushButton_2.clicked.connect(excluir_dados)
tela_admin.pushButton_3.clicked.connect(editar_dados)

tela_editar.pushButton.clicked.connect(logout_editar)
tela_editar.pushButton_2.clicked.connect(salvar_edicao)
tela_principal.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

tela_principal.show()
app.exec()
