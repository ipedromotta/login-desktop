import pytest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) # Para conseguir ler o módulo usuario.

from Model.UsuarioModel import UsuarioModel


# === FIXTURES (ajudam a criar dados/mocks reutilizáveis) ===

@pytest.fixture
def mock_session():
    """Cria uma sessão falsa (mockada) para simular acesso ao banco de dados."""
    mock = MagicMock()
    return mock

@pytest.fixture
def usuario_instancia():
    """Cria uma instância do modelo para testes."""
    return UsuarioModel(nome="Fulano", usuario="fulano123", senha="senha_segura")


# === TESTE DO CONSTRUTOR (init) ===

@patch("Model.UsuarioModel.Criptografia.criptografar", return_value="senha_hash")
def test_init_usuario_model(mock_criptografar):
    """Verifica se o construtor criptografa a senha corretamente ao instanciar."""
    usuario = UsuarioModel("Nome", "usuario", "senha")
    assert usuario.nome == "Nome"
    assert usuario.usuario == "usuario"
    assert usuario.senha == "senha_hash"
    assert not usuario.administrador  # valor padrão
    mock_criptografar.assert_called_once_with("senha")


# === TESTES DE MÉTODO logar ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
@patch("Model.UsuarioModel.Criptografia.verificar_senha", return_value=True)
def test_logar_usuario_valido(mock_verificar, mock_connection):
    """Testa login válido retornando um usuário simulado."""
    # Simula a sessão de banco de dados
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session

    # Simula o retorno do banco
    mock_usuario = MagicMock()
    mock_session.scalars.return_value.first.return_value = mock_usuario

    usuario = UsuarioModel.logar("usuario", "senha")
    assert usuario == mock_usuario
    mock_verificar.assert_called_once()


@patch("Model.UsuarioModel.FactoryConnection.get_connection")
@patch("Model.UsuarioModel.Criptografia.verificar_senha", return_value=False)
def test_logar_senha_invalida(mock_verificar, mock_connection):
    """Testa login com senha incorreta, deve retornar None."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session
    mock_session.scalars.return_value.first.return_value = MagicMock()

    usuario = UsuarioModel.logar("usuario", "senha_errada")
    assert usuario is None


# === TESTE DE EXISTÊNCIA DO USUÁRIO ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
def test_usuario_existe(mock_connection):
    """Verifica se o método detecta a existência de um usuário."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session
    mock_session.scalars.return_value.first.return_value = True

    assert UsuarioModel.usuario_existe("usuario") is True


# === TESTES DE CADASTRO ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
@patch("Model.UsuarioModel.Criptografia.criptografar", return_value="senha_hash")
def test_cadastrar_usuario_sucesso(mock_criptografar, mock_connection):
    """Testa cadastro bem-sucedido de um novo usuário."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session

    sucesso = UsuarioModel.cadastrar("Nome", "usuario", "senha")
    assert sucesso is True
    mock_session.add.assert_called()
    mock_session.commit.assert_called()


def test_cadastrar_usuario_campos_vazios():
    """Testa tentativa de cadastro com campos faltando."""
    assert not UsuarioModel.cadastrar("", "usuario", "senha")
    assert not UsuarioModel.cadastrar("Nome", "", "senha")
    assert not UsuarioModel.cadastrar("Nome", "usuario", "")


# === TESTES DE LISTAGEM ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
def test_listar_usuarios(mock_connection):
    """Testa a listagem de usuários no banco."""
    mock_session = MagicMock()
    usuarios_fake = [MagicMock(), MagicMock()]
    mock_connection.return_value.__enter__.return_value = mock_session
    mock_session.scalars.return_value.all.return_value = usuarios_fake

    resultado = UsuarioModel.listar_usuarios()
    assert resultado == usuarios_fake


# === TESTE DE CONSULTA POR ID ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
def test_consultar_usuario(mock_connection):
    """Testa a consulta de um usuário por ID."""
    mock_session = MagicMock()
    usuario_fake = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session
    mock_session.scalars.return_value.first.return_value = usuario_fake

    resultado = UsuarioModel.consultar_usuario(1)
    assert resultado == usuario_fake


# === TESTE DE ATUALIZAÇÃO ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
@patch("Model.UsuarioModel.Criptografia.criptografar", return_value="senha_nova_hash")
def test_atualizar_usuario(mock_criptografar, mock_connection):
    """Testa a atualização dos dados de um usuário."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session

    resultado = UsuarioModel.atualizar_usuario(1, "Novo Nome", "novo_user", "senha_nova", True)
    assert resultado is True
    mock_session.execute.assert_called()
    mock_session.commit.assert_called()


# === TESTE DE EXCLUSÃO ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
def test_excluir_usuario(mock_connection):
    """Testa a exclusão de um usuário por ID."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session

    resultado = UsuarioModel.excluir_usuario(1)
    assert resultado is True
    mock_session.execute.assert_called()
    mock_session.commit.assert_called()


# === TESTE DE VERIFICAÇÃO DE ADMINISTRADOR ===

@patch("Model.UsuarioModel.FactoryConnection.get_connection")
def test_verificar_admin_cria_admin(mock_connection):
    """Verifica se o método cria um admin se não existir nenhum."""
    mock_session = MagicMock()
    mock_connection.return_value.__enter__.return_value = mock_session

    # Simula que nenhum admin existe no banco
    mock_session.query.return_value.filter_by.return_value.first.return_value = None

    UsuarioModel.verificar_admin()
    mock_session.add.assert_called()
    mock_session.commit.assert_called()
