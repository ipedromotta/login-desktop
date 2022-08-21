from Controller.ConnectionDBController import ConnectionDBController

from Model.AdminModel import AdminModel
from Model.UsuarioModel import UsuarioModel


class AcoesController:
    def __init__(self) -> None:
        self.cnxn = ConnectionDBController.get_connection()
    
    def cadastrar(self, interface, nome:str, usuario:str, senha:str) -> None:
        if usuario == "" or senha == "" or nome == "":
            interface.msg_cadastro.emit("Preencha todos os campos!")
            return

        usuario_existe = UsuarioModel.usuario_existe(usuario, self.cnxn)
        if usuario_existe:
            interface.msg_cadastro.emit("Este usuário já está sendo utilizado!")
            return

        cadastrou = UsuarioModel.cadastrar(nome, usuario, senha, self.cnxn)

        interface.limpar_cadastro.emit()

        if cadastrou:
            interface.msg_cadastro.emit("Usuário cadastrado com sucesso!")
        else:
            interface.msg_cadastro.emit("Usuário não foi cadastrado")
            
    def consultar_cadastros(self) -> None:
        return AdminModel.consultar_usuarios(self.cnxn)

    def editar_dados(self, dados_lidos:dict, usuario_selecionado:int, ui, tela_admin) -> None:
        if dados_lidos:
            numero_id = dados_lidos[usuario_selecionado][0]
            usuario_antigo = dados_lidos[usuario_selecionado][2]
            usuario = AdminModel.consultar_usuario(numero_id, self.cnxn)

            if usuario:
                ui.novo_nome.setText(str(usuario[0][1]))
                ui.novo_usuario.setText(str(usuario[0][2]))
                if usuario[0][4] == 1:
                    ui.bl_admin.setChecked(True)

                ui.btn_salvar.clicked.connect(lambda: self.salvar_edicao(ui, usuario_antigo, numero_id, tela_admin))

    def salvar_edicao(self, ui, usuario_antigo:str, numero_id:int, tela_admin) -> None:
        nome = ui.novo_nome.text()
        usuario = ui.novo_usuario.text()
        senha = ui.nova_senha.text()
        admin = ui.bl_admin.isChecked()

        if usuario == '' or senha == '' or nome == '':
            ui.lbl_erro.setText("Preencha todos os dados!")
            return

        if usuario_antigo != usuario:
            usuario_existe = UsuarioModel.usuario_existe(usuario, self.cnxn)
            if usuario_existe:
                ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
                return

        atualizou = AdminModel.atualizar_usuario(nome, usuario, senha, admin, numero_id, self.cnxn)
        if not atualizou:
            ui.lbl_erro.setText("Atualização falhou!")
            return
        
        tela_admin()

    def excluir_dados(self, dados_lidos:dict, usuario_selecionado:int) -> None:
        numero_id = dados_lidos[usuario_selecionado][0]
        AdminModel.excluir_usuario(numero_id, self.cnxn)

