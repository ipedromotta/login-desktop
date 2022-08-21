from cryptography.fernet import Fernet


class CriptografiaController:
    def __init__(self):
        self.__chave = b'8g_HV2iOzb0FZjDo4a9iLfj4WkWm4m3pv797GRplmqE=' # Calma, isto é apenas um teste.
        self.__fernet = Fernet(self.__chave)

    def criptografar(self, senha:str) -> str|bool:
        try:
            senha_encriptografada = self.__fernet.encrypt(senha.encode())
            return senha_encriptografada.decode()
        except:
            return False

    def descriptografar(self, cripto:str, senha:str) -> bool:
        try:
            senha_descriptografada = self.__fernet.decrypt(cripto.encode()).decode()
            return senha_descriptografada == senha
        except:
            return False
