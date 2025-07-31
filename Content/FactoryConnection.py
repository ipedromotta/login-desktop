from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from Content.Log import logger
from Model.BaseModel import Base
from Model.Configuration import Configuration


class FactoryConnection:
    __engine = None
    __session = None

    @classmethod
    def _initialize(cls):
        try:
            if cls.__engine is None:
                logger.info("Criando pool de conexão")
                
                host, database, user, password = Configuration().database

                connection_url = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

                cls.__engine = create_engine(
                    connection_url,
                    poolclass=QueuePool,
                    pool_size=5,
                    max_overflow=10,
                    pool_pre_ping=True,
                    echo=False,  # Opcional: mostra logs SQL
                )
                cls.__session = sessionmaker(bind=cls.__engine)
                
                Base.metadata.create_all(cls.__engine)
                
                logger.info("pool de conexão criada com sucesso")
        except Exception as e:
            logger.error(f"Erro ao criar pool de conexões {e}", exc_info=True)

    @classmethod
    def get_connection(cls):
        cls._initialize()
        return cls.__session()
