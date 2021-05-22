from PyQt5 import uic, QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="usuarios"
)

numero_id = 0


def excluir_dados():
    linha = tela_admin.tableWidget.currentRow()
    tela_admin.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM dados")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM dados WHERE id =" + str(valor_id))


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

    tela_editar.close()
    tela_admin.close()
    admin()


def logout_editar():
    tela_editar.close()
    tela_editar.lineEdit.setText("")
    tela_editar.lineEdit_2.setText("")


def cadastrar():
    usuario = cadastro.lineEdit.text()
    senha = cadastro.lineEdit_2.text()

    if usuario == "" or senha == "":
        cadastro.label_5.setText("Preencha todos os campos!")
        return

    cadastro.label_4.setText("Usuário cadastrado com sucesso!")
    cadastro.label_5.setText("")
    cursor = banco.cursor()
    query = "INSERT INTO dados (usuario, senha) VALUES (%s,%s)"
    info = (str(usuario), str(senha))
    cursor.execute(query, info)
    banco.commit()
    cadastro.lineEdit.setText("")
    cadastro.lineEdit_2.setText("")


def sair():
    cadastro.label_4.setText("")
    cadastro.label_5.setText("")
    cadastro.close()
    primeira_tela.show()


def inicio():
    primeira_tela.close()
    cadastro.show()


def login():
    primeira_tela.label_3.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    cursor = banco.cursor()
    query = "SELECT usuario, senha FROM dados WHERE usuario like'" + \
        nome_usuario+"' and senha like '" + senha + "'"
    cursor.execute(query)
    resultado = cursor.fetchone()

    if resultado == None:
        primeira_tela.label_3.setText("Login ou senha incorreto!")
    elif nome_usuario == "admin" and senha == "admin":
        primeira_tela.lineEdit.setText("")
        primeira_tela.lineEdit_2.setText("")
        primeira_tela.close()
        tela_admin.show()
        admin()

    else:
        primeira_tela.lineEdit.setText("")
        primeira_tela.lineEdit_2.setText("")
        primeira_tela.close()
        segunda_tela.show()


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
    segunda_tela.close()
    tela_admin.close()
    primeira_tela.show()


app = QtWidgets.QApplication([])
cadastro = uic.loadUi("cadastro.ui")
primeira_tela = uic.loadUi("primeira_tela.ui")
segunda_tela = uic.loadUi("segunda_tela.ui")
tela_admin = uic.loadUi("tela_admin.ui")
tela_editar = uic.loadUi("tela_editar.ui")
cadastro.pushButton.clicked.connect(cadastrar)
cadastro.pushButton_2.clicked.connect(sair)
primeira_tela.pushButton_2.clicked.connect(inicio)
primeira_tela.pushButton.clicked.connect(login)
segunda_tela.pushButton.clicked.connect(logout)
tela_admin.pushButton.clicked.connect(logout)
tela_admin.pushButton_2.clicked.connect(excluir_dados)
tela_admin.pushButton_3.clicked.connect(editar_dados)

tela_editar.pushButton.clicked.connect(logout_editar)
tela_editar.pushButton_2.clicked.connect(salvar_edicao)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
cadastro.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

primeira_tela.show()
app.exec()
