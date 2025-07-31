from PyQt5 import QtCore, QtWidgets

from Content.Log import logger
from View.Admin import Ui_Admin
from Model.UsuarioModel import UsuarioModel
from Controller.EdicaoController import EdicaoController


class AdministradorController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self.edicao_controller = EdicaoController()
        self.dados_lidos = []

        self.iniciar_eventos()
        self.carregar_dados()
        
    def iniciar_eventos(self):
        logger.info("Iniciando eventos da pagina - administrador")
        self.ui.btn_logout.clicked.connect(self.voltar)
        self.ui.btn_editar.clicked.connect(self.editar_dados)
        self.ui.btn_excluir.clicked.connect(self.excluir_usuario)
        self.edicao_controller.voltar_tela.connect(self.show)
        self.edicao_controller.voltar_tela.connect(self.carregar_dados)
        
    def carregar_dados(self):
        try:
            logger.info("Carregando dados - admnistrador")
            self.dados_lidos = UsuarioModel.listar_usuarios()
            qtd_dados = len(self.dados_lidos)
            
            self.ui.tbl_usuarios.setRowCount(qtd_dados)
            self.ui.tbl_usuarios.setColumnCount(3)
            for linha, usuario in enumerate(self.dados_lidos):
                self.ui.tbl_usuarios.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(usuario.id)))
                self.ui.tbl_usuarios.setItem(linha, 1, QtWidgets.QTableWidgetItem(usuario.nome))
                self.ui.tbl_usuarios.setItem(linha, 2, QtWidgets.QTableWidgetItem(usuario.usuario))
                    
        except Exception as e:
            logger.error(f"Erro ao carregar dados - administrador {e}", exc_info=True)
        
    def editar_dados(self) -> None:
        try:
            logger.info("Editando dados - administrador")
            usuario_selecionado = self.ui.tbl_usuarios.currentRow()
            usuario_selecionado = self.dados_lidos[usuario_selecionado]
            self.close()
            self.edicao_controller.carregar_tela(usuario_selecionado)
            self.edicao_controller.show()
            
        except Exception as e:
            logger.error(f"Erro ao editar dados - administrador {e}", exc_info=True)
        
    def excluir_usuario(self) -> None:
        try:
            logger.info("Excluindo dados - administrador")
            usuario_selecionado = self.ui.tbl_usuarios.currentRow()
            self.ui.tbl_usuarios.removeRow(usuario_selecionado)
            
            usuario = self.dados_lidos[usuario_selecionado]
            UsuarioModel.excluir_usuario(usuario.id)
            self.carregar_dados()
        except Exception as e:
            logger.error(f"Erro ao excluir usuario - administrador {e}", exc_info=True)
    
    def voltar(self):
        self.close()
        self.voltar_tela.emit()
