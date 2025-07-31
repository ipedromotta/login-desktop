from PyQt5 import QtCore, QtWidgets

from Content.Log import logger
from View.Edicao import Ui_Edicao
from Model.UsuarioModel import UsuarioModel


class EdicaoController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Edicao()
        self.ui.setupUi(self)
        self._usuario_editado = None
        self.ui.btn_cancelar.clicked.connect(self.voltar)
        self.ui.btn_salvar.clicked.connect(self.salvar_edicao)
        
    def carregar_tela(self, usuario_selecionado:UsuarioModel) -> None:
        logger.info("Carregando tela de edição")
        self.ui.nova_senha.setText("")
        self._usuario_editado = usuario_selecionado
        self.ui.novo_nome.setText(str(usuario_selecionado.nome))
        self.ui.novo_usuario.setText(str(usuario_selecionado.usuario))
        self.ui.bl_admin.setChecked(usuario_selecionado.administrador)

    def salvar_edicao(self) -> None:
        logger.info("Salvando edição...")
        nome = self.ui.novo_nome.text()
        usuario = self.ui.novo_usuario.text()
        senha = self.ui.nova_senha.text()
        admin = self.ui.bl_admin.isChecked()

        if usuario == '' or senha == '' or nome == '':
            logger.warning("Tentativa de edição com campos vazios")
            self.ui.lbl_erro.setText("Preencha todos os dados!")
            return

        if self._usuario_editado.usuario != usuario:
            usuario_existe = UsuarioModel.usuario_existe(usuario)
            if usuario_existe:
                logger.warning("Este usuário já está sendo utilizado!")
                self.ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
                return

        atualizou = UsuarioModel.atualizar_usuario(self._usuario_editado.id, nome, usuario, senha, admin)
        if not atualizou:
            logger.warning("Atualização falhou!")
            self.ui.lbl_erro.setText("Atualização falhou!")
            return
        else:
            logger.info("Usuário editado com sucesso")
            self.voltar()
    
    def voltar(self):
        self.close()
        self.voltar_tela.emit()
    