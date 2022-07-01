# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_editar.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaEdicao(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 220)
        MainWindow.setMinimumSize(QtCore.QSize(415, 220))
        MainWindow.setMaximumSize(QtCore.QSize(415, 220))
        MainWindow.setStyleSheet("background-color: rgb(57, 130, 195);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_edite_dados = QtWidgets.QLabel(self.centralwidget)
        self.lbl_edite_dados.setGeometry(QtCore.QRect(70, 10, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_edite_dados.setFont(font)
        self.lbl_edite_dados.setStyleSheet("color: white;")
        self.lbl_edite_dados.setObjectName("lbl_edite_dados")
        self.novo_usuario = QtWidgets.QLineEdit(self.centralwidget)
        self.novo_usuario.setGeometry(QtCore.QRect(80, 60, 113, 31))
        self.novo_usuario.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 8px;")
        self.novo_usuario.setObjectName("novo_usuario")
        self.nova_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.nova_senha.setGeometry(QtCore.QRect(220, 60, 113, 31))
        self.nova_senha.setStyleSheet("background-color: white;\n"
"border-radius: 15px;\n"
"padding: 8px;")
        self.nova_senha.setObjectName("nova_senha")
        self.btn_cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancelar.setGeometry(QtCore.QRect(150, 169, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_cancelar.setFont(font)
        self.btn_cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancelar.setStyleSheet("background-color: rgb(237, 212, 0);\n"
"border-radius: 15px;\n"
"")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_salvar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_salvar.setGeometry(QtCore.QRect(150, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.btn_salvar.setFont(font)
        self.btn_salvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_salvar.setStyleSheet("background-color: #6EC8DB;\n"
"border-radius: 15px;\n"
"")
        self.btn_salvar.setObjectName("btn_salvar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.novo_usuario, self.nova_senha)
        MainWindow.setTabOrder(self.nova_senha, self.btn_salvar)
        MainWindow.setTabOrder(self.btn_salvar, self.btn_cancelar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Edição"))
        self.lbl_edite_dados.setText(_translate("MainWindow", "Edite os dados do usuário"))
        self.novo_usuario.setPlaceholderText(_translate("MainWindow", "Novo usuário"))
        self.nova_senha.setPlaceholderText(_translate("MainWindow", "Nova senha"))
        self.btn_cancelar.setText(_translate("MainWindow", "CANCELAR"))
        self.btn_salvar.setText(_translate("MainWindow", "SALVAR"))