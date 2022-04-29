class AcoesController:
    def cadastrar(self, cnxn, ui, usuario, senha):
        if usuario == "" or senha == "":
            ui.lbl_erro.setText("Preencha todos os campos!")
            return

        cursor = cnxn.cursor()
        query = "INSERT INTO dados (usuario, senha) VALUES (%s, %s)"
        info = (usuario, senha)
        try:
            cursor.execute(query, info)
            cnxn.commit()
        except Exception as ex:
            return ex

        ui.lbl_msg.setText("Usuário cadastrado com sucesso!")
        ui.lbl_erro.setText("")
        ui.usuario.setText("")
        ui.senha.setText("")

    def editar_dados(self, cnxn, ui, tela_admin, tela, funcao_tela_admin):
        ui.setupUi(tela)
        tela.show()
        linha = tela_admin.tbl_usuarios.currentRow()

        cursor = cnxn.cursor()
        cursor.execute("SELECT id FROM dados")
        dados_lidos = cursor.fetchall()
        numero_id = dados_lidos[linha][0]
        cursor.execute("SELECT * FROM dados WHERE id =" + str(numero_id))
        usuario = cursor.fetchall()

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

        cursor = cnxn.cursor()
        cursor.execute("UPDATE dados SET usuario = '{}', senha = '{}' WHERE id = {}".format(
                        usuario, senha, numero_id))
        cnxn.commit()
        funcao_tela_admin(tela)

    def excluir_dados(self, cnxn, tela_admin):
        linha = tela_admin.tbl_usuarios.currentRow()
        tela_admin.tbl_usuarios.removeRow(linha)

        cursor = cnxn.cursor()
        cursor.execute("SELECT id FROM dados")
        dados_lidos = cursor.fetchall()
        numero_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM dados WHERE id =" + str(numero_id))
        cnxn.commit()
        