from PyQt5 import QtCore, QtWidgets

from View.Admin import Ui_Admin
from Model.AdminModel import AdminModel
from Controller.EdicaoController import EdicaoController


class AdministradorController(QtWidgets.QMainWindow):
    voltar_tela = QtCore.pyqtSignal()
    
    def __init__(self, conn=None) -> None:
        super().__init__()
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self._conn = conn
        self.edicao_controller = EdicaoController(self._conn)
        
        self.iniciar_eventos()
        self.carregar_dados()
        
    def iniciar_eventos(self):
        self.ui.btn_logout.clicked.connect(self.voltar)
        
    def carregar_dados(self):
        try:
            dados_lidos = AdminModel.consultar_usuarios(self._conn)
            
            self.ui.tbl_usuarios.setRowCount(len(dados_lidos))
            self.ui.tbl_usuarios.setColumnCount(3)
            for linha in range(0, len(dados_lidos)):
                for coluna in range(0, 3):
                    item = QtWidgets.QTableWidgetItem(str(dados_lidos[linha][coluna]))
                    item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    self.ui.tbl_usuarios.setItem(linha, coluna, item)
                    
            self.ui.btn_editar.clicked.connect(lambda: self.editar_dados(dados_lidos))
            self.ui.btn_excluir.clicked.connect(lambda: self.excluir_usuario(dados_lidos))
        except Exception as ex:
            print(ex)
        
    def editar_dados(self, dados_lidos:dict) -> None:
        try:
            usuario_selecionado = self.ui.tbl_usuarios.currentRow()
            self.close()
            self.edicao_controller.voltar_tela.connect(self.show)
            self.edicao_controller.voltar_tela.connect(self.carregar_dados)
            self.edicao_controller.carregar_tela(dados_lidos, usuario_selecionado)
            self.edicao_controller.show()
            
        except Exception as ex:
            print(ex)
        
    def excluir_usuario(self, dados_lidos:dict) -> None:
        try:
            usuario_selecionado = self.ui.tbl_usuarios.currentRow()
            self.ui.tbl_usuarios.removeRow(usuario_selecionado)
            
            numero_id = dados_lidos[usuario_selecionado][0]
            AdminModel.excluir_usuario(numero_id, self._conn)
        except Exception as ex:
            print(ex)
    
    def voltar(self):
        self.close()
        self.voltar_tela.emit()
