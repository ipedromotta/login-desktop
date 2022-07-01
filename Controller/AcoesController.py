from Model.AdminModel import AdminModel
from Model.UsuarioModel import UsuarioModel


class AcoesController:
    def cadastrar(self, cnxn, ui, usuario, senha):
        if usuario == "" or senha == "":
            ui.lbl_erro.setText("Preencha todos os campos!")
            return

        cadastrou = UsuarioModel.cadastrar(usuario, senha, cnxn)

        ui.lbl_erro.setText("")
        ui.usuario.setText("")
        ui.senha.setText("")

        if cadastrou:
            ui.lbl_msg.setText("Usuário cadastrado com sucesso!")
        else:
            ui.lbl_msg.setText("Usuário não foi cadastrado")

    def editar_dados(self, cnxn, ui, tela_admin, tela, funcao_tela_admin):
        ui.setupUi(tela)
        tela.show()
        linha = tela_admin.tbl_usuarios.currentRow()

        dados_lidos = AdminModel.consultar_usuarios(cnxn)
        if dados_lidos:
            numero_id = dados_lidos[linha][0]
            usuario = AdminModel.consultar_usuario(numero_id, cnxn)

            if usuario:
                ui.novo_usuario.setText(str(usuario[0][1]))
                ui.nova_senha.setText(str(usuario[0][2]))

                ui.btn_salvar.clicked.connect(lambda: self.salvar_edicao(cnxn, tela, ui, usuario[0][1], usuario[0][2], numero_id, funcao_tela_admin))
                ui.btn_cancelar.clicked.connect(lambda: funcao_tela_admin(tela))

    def salvar_edicao(self, cnxn, tela, ui, usuario_antigo, senha_antiga, numero_id, funcao_tela_admin):
        usuario = ui.novo_usuario.text()
        senha = ui.nova_senha.text()

        if usuario == '':
            usuario = usuario_antigo
        if senha == '':
            senha = senha_antiga

        AdminModel.atualizar_usuario(usuario, senha, numero_id, cnxn)
        funcao_tela_admin(tela)

    def excluir_dados(self, cnxn, tela_admin):
        linha = tela_admin.tbl_usuarios.currentRow()
        tela_admin.tbl_usuarios.removeRow(linha)

        dados_lidos = AdminModel.consultar_usuarios(cnxn)
        numero_id = dados_lidos[linha][0]
        AdminModel.excluir_usuario(numero_id, cnxn)
