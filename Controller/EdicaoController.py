from PyQt5 import QtCore, QtWidgets

from View.Edicao import Ui_Edicao
from Model.UsuarioModel import UsuarioModel
from Model.AdminModel import AdminModel


class EdicaoController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self, conn=None) -> None:
        super().__init__()
        self.ui = Ui_Edicao()
        self.ui.setupUi(self)
        self.ui.btn_cancelar.clicked.connect(self.voltar)
        self._conn = conn
        
    def carregar_tela(self, dados_lidos:dict, usuario_selecionado:int) -> None:
        if dados_lidos:
            numero_id = dados_lidos[usuario_selecionado][0]
            usuario_antigo = dados_lidos[usuario_selecionado][2]
            usuario = AdminModel.consultar_usuario(numero_id, self._conn)

            if usuario:
                self.ui.novo_nome.setText(str(usuario[0][1]))
                self.ui.novo_usuario.setText(str(usuario[0][2]))
                self.ui.nova_senha.setText("")
                if usuario[0][4] == 1:
                    self.ui.bl_admin.setChecked(True)
                else:
                    self.ui.bl_admin.setChecked(False)

                self.ui.btn_salvar.clicked.connect(lambda: self.salvar_edicao(usuario_antigo, numero_id))
        
    def salvar_edicao(self, usuario_antigo:str, numero_id:int) -> None:
        nome = self.ui.novo_nome.text()
        usuario = self.ui.novo_usuario.text()
        senha = self.ui.nova_senha.text()
        admin = self.ui.bl_admin.isChecked()

        if usuario == '' or senha == '' or nome == '':
            self.ui.lbl_erro.setText("Preencha todos os dados!")
            return

        if usuario_antigo != usuario:
            usuario_existe = UsuarioModel.usuario_existe(usuario, self._conn)
            if usuario_existe:
                self.ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
                return

        atualizou = AdminModel.atualizar_usuario(nome, usuario, senha, admin, numero_id, self._conn)
        if not atualizou:
            self.ui.lbl_erro.setText("Atualização falhou!")
            return
        else:
            self.voltar()
    
    def voltar(self):
        self.close()
        self.voltar_tela.emit()
    