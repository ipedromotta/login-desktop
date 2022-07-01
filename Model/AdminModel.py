class AdminModel:

    @staticmethod
    def consultar_usuarios(conn):
        try:
            query = "SELECT * FROM dados"
            cursor = conn.cursor()
            cursor.execute(query)
            usuarios = cursor.fetchall()

            return usuarios
        except:
            return None

    @staticmethod
    def consultar_usuario(id, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM dados WHERE id =" + str(id))
            usuario = cursor.fetchall()
            
            return usuario
        except:
            return None

    @staticmethod
    def atualizar_usuario(usuario, senha, numero_id, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE dados SET usuario = '{}', senha = '{}' WHERE id = {}".format(
                        usuario, senha, numero_id))
            conn.commit()

        except Exception as ex:
            print(ex)

    @staticmethod
    def excluir_usuario(id, conn):
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM dados WHERE id =" + str(id))
            cursor.commit()
        except Exception as ex:
            print(f'Erro ao deletar: {ex}')