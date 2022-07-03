from Model.AdminModel import AdminModel
from Model.UsuarioModel import UsuarioModel


class AcoesController:
    def cadastrar(self, cnxn, ui, nome, usuario, senha):
        if usuario == "" or senha == "" or nome == "":
            ui.lbl_erro.setText("Preencha todos os campos!")
            return

        usuario_existe = UsuarioModel.usuario_existe(usuario, cnxn)
        if usuario_existe:
            ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
            return

        cadastrou = UsuarioModel.cadastrar(nome, usuario, senha, cnxn)

        ui.lbl_erro.setText("")
        ui.nome.setText("")
        ui.usuario.setText("")
        ui.senha.setText("")

        if cadastrou:
            ui.lbl_erro.setText("Usuário cadastrado com sucesso!")
        else:
            ui.lbl_erro.setText("Usuário não foi cadastrado")

    def editar_dados(self, cnxn, ui, tela_admin, tela, funcao_tela_admin):
        ui.setupUi(tela)
        tela.show()
        linha = tela_admin.tbl_usuarios.currentRow()

        dados_lidos = AdminModel.consultar_usuarios(cnxn)
        if dados_lidos:
            numero_id = dados_lidos[linha][0]
            usuario_antigo = dados_lidos[linha][2]
            usuario = AdminModel.consultar_usuario(numero_id, cnxn)

            if usuario:
                ui.novo_nome.setText(str(usuario[0][1]))
                ui.novo_usuario.setText(str(usuario[0][2]))
                if usuario[0][4] == 1:
                    ui.bl_admin.setChecked(True)

                ui.btn_salvar.clicked.connect(lambda: self.salvar_edicao(cnxn, tela, ui, usuario_antigo, numero_id, funcao_tela_admin))
                ui.btn_cancelar.clicked.connect(lambda: funcao_tela_admin(tela))

    def salvar_edicao(self, cnxn, tela, ui, usuario_antigo, numero_id, funcao_tela_admin):
        nome = ui.novo_nome.text()
        usuario = ui.novo_usuario.text()
        senha = ui.nova_senha.text()
        admin = ui.bl_admin.isChecked()

        if usuario == '' or senha == '' or nome == '':
            ui.lbl_erro.setText("Preencha todos os dados!")
            return

        if usuario_antigo != usuario:
            usuario_existe = UsuarioModel.usuario_existe(usuario, cnxn)
            if usuario_existe:
                ui.lbl_erro.setText("Este usuário já está sendo utilizado!")
                return

        atualizou = AdminModel.atualizar_usuario(nome, usuario, senha, admin, numero_id, cnxn)
        if not atualizou:
            ui.lbl_erro.setText("Atualização falhou!")
            return

        funcao_tela_admin(tela)

    def excluir_dados(self, cnxn, tela_admin):
        linha = tela_admin.tbl_usuarios.currentRow()
        tela_admin.tbl_usuarios.removeRow(linha)

        dados_lidos = AdminModel.consultar_usuarios(cnxn)
        numero_id = dados_lidos[linha][0]
        AdminModel.excluir_usuario(numero_id, cnxn)
