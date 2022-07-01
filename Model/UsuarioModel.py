
class UsuarioModel():
    def __init__(self, id=None, usuario=None, bl_adm=None):
        self.Id = id
        self.Usuario = usuario
        self.Administrador = True if bl_adm == 1 else False

    def logar(self, login, senha, conn):
        try:
            cursor = conn.cursor(dictionary=True)

            query = f"SELECT * FROM dados WHERE usuario ='{login}' and senha = '{senha}'"
            cursor.execute(query)
            row = cursor.fetchone()
            del row['senha']
            obj = UsuarioModel(**row)
            cursor.close()

            return obj
        except Exception as e:
            return None

    @staticmethod
    def cadastrar(usuario, senha, conn):
        cursor = conn.cursor()
        query = "INSERT INTO dados (usuario, senha) VALUES (%s, %s)"
        info = (usuario, senha)
        try:
            cursor.execute(query, info)
            conn.commit()
            return True
        except:
            return False

