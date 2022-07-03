from Controller.CriptografiaController import CriptografiaController


class UsuarioModel():
    def __init__(self, ID=None, NOME=None, USUARIO=None, BL_ADM=None):
        self.Id = ID
        self.Nome = NOME
        self.Usuario = USUARIO
        self.Administrador = True if BL_ADM == 1 else False

    def logar(self, login, senha, conn):
        try:
            cursor = conn.cursor(dictionary=True)

            query = f"SELECT * FROM dados WHERE USUARIO ='{login}'"
            cursor.execute(query)
            row = cursor.fetchone()
            usuario_valido = CriptografiaController().descriptografar(row['SENHA'], senha)
            if usuario_valido:
                del row['SENHA']
                obj = UsuarioModel(**row)
                cursor.close()
                return obj

            return None
        except Exception as e:
            return None

    @staticmethod
    def cadastrar(nome, usuario, senha, conn):
        senha_criptografada = CriptografiaController().criptografar(senha)
        if not senha_criptografada:
            return False

        cursor = conn.cursor()
        query = "INSERT INTO dados (NOME, USUARIO, SENHA) VALUES (%s, %s, %s)"
        info = (nome, usuario, senha_criptografada)
        try:
            cursor.execute(query, info)
            conn.commit()
            return True
        except:
            return False

    @staticmethod
    def usuario_existe(login, conn):
        cursor = conn.cursor()
        query = f"SELECT * FROM dados WHERE USUARIO ='{login}'"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            return True
            
        return False
