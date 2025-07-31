from sqlalchemy import Column, Integer, String, Boolean, select, update, delete

from Content.Log import logger
from Model.BaseModel import Base
from Content.Criptografia import Criptografia
from Content.FactoryConnection import FactoryConnection


class UsuarioModel(Base):
    __tablename__ = 'dados'

    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(100), nullable=False)
    usuario = Column('USUARIO', String(50), unique=True, nullable=False)
    senha = Column('SENHA', String(200), nullable=False)
    administrador = Column('BL_ADM', Boolean, default=False)

    def __init__(self, nome, usuario, senha, administrador=False):
        self.nome = nome
        self.usuario = usuario
        self.senha = Criptografia.criptografar(senha)
        self.administrador = administrador

    @classmethod
    def logar(cls, login: str, senha: str) -> "UsuarioModel":
        try:
            stmt = select(cls).where(cls.usuario == login)
            with FactoryConnection.get_connection() as session:
                usuario = session.scalars(stmt).first()

            if usuario and Criptografia.verificar_senha(senha, usuario.senha):
                return usuario
            return None
        except Exception as e:
            logger.error(f"Falha ao logar: {e}", exc_info=True)
            return None

    @classmethod
    def usuario_existe(cls, login: str) -> bool:
        with FactoryConnection.get_connection() as session:
            stmt = select(cls).where(cls.usuario == login)
            return session.scalars(stmt).first() is not None

    @classmethod
    def cadastrar(cls, nome: str, usuario: str, senha: str) -> bool:
        try:
            if not nome or not usuario or not senha:
                return False
            
            with FactoryConnection.get_connection() as session:
                novo_usuario = cls(nome, usuario, senha)
                session.add(novo_usuario)
                session.commit()
                return True
        except Exception as e:
            logger.error(f"Falha ao cadastrar: {e}", exc_info=True)
            return False

    # --- ADMIN: Listar todos os usuários ---
    @classmethod
    def listar_usuarios(cls) -> list["UsuarioModel"]:
        """Retorna todos os usuários, se o usuário for admin."""
        try:
            with FactoryConnection.get_connection() as session:
                stmt = select(cls)
                return session.scalars(stmt).all()
        except Exception as e:
            logger.error(f"Falha ao listar usuários: {e}", exc_info=True)
            return None

    # --- ADMIN: Consultar usuário por ID ---
    @classmethod
    def consultar_usuario(cls, id: int) -> "UsuarioModel":
        try:
            with FactoryConnection.get_connection() as session:
                stmt = select(cls).where(cls.id == id)
                return session.scalars(stmt).first()
        except Exception as e:
            logger.error(f"Falha ao consultar usuário: {e}", exc_info=True)
            return None

    # --- ADMIN: Atualizar usuário ---
    @classmethod
    def atualizar_usuario(cls, id: int, nome: str, usuario: str, senha: str, admin: bool) -> bool:
        try:
            senha_criptografada = Criptografia.criptografar(senha)
            with FactoryConnection.get_connection() as session:
                stmt = (
                    update(cls)
                    .where(cls.id == id)
                    .values(nome=nome, usuario=usuario, senha=senha_criptografada, administrador=admin)
                )
                session.execute(stmt)
                session.commit()
                return True
        except Exception as e:
            logger.error(f"Falha ao atualizar usuário: {e}", exc_info=True)
            return False

    # --- ADMIN: Excluir usuário ---
    @classmethod
    def excluir_usuario(cls, id: int) -> bool:
        try:
            with FactoryConnection.get_connection() as session:
                stmt = delete(cls).where(cls.id == id)
                session.execute(stmt)
                session.commit()
                return True
        except Exception as e:
            logger.error(f"Falha ao excluir usuário: {e}", exc_info=True)
            return False
        
    @classmethod
    def verificar_admin(cls) -> None:
        # Verifica se já existe um administrador cadastrado
        try:
            with FactoryConnection.get_connection() as session:
                existe_admin = session.query(UsuarioModel).filter_by(administrador=True).first()

                if not existe_admin:
                    logger.info("Usuário administrador não existe no banco, criando...")
                    admin = UsuarioModel(
                        nome="Administrador",
                        usuario="admin",
                        senha="123",
                        administrador=True
                    )
                    session.add(admin)
                    session.commit()
                    logger.info("Usuário administrador criado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao verificar/criar admin: {e}", exc_info=True)
    