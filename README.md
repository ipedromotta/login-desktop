<h1 align="center">
<img src="https://github.com/ipedromotta/VueJS-Flask/blob/main/frontend/src/assets/logo-python.png" width="50"><br>Sistema de login Python/MySQL
</h1>

## 📄 Sobre #

<p> 
Este projeto é um sistema de login desktop com funcionalidades CRUD (Create, Read, Update, Delete), desenvolvido em Python com interface gráfica usando PyQt5 e QtDesigner.

A aplicação gerencia usuários e permissões administrativas diretamente na interface, permitindo acesso especial para usuários com o campo **bl_adm** configurado como **True**.
</p>

## ⚙️ Configuração do projeto 

### Requisitos
- MySQL rodando localmente ou remotamente
- Python 3.x instalado

### Configuração da Conexão com o Banco
A conexão com o banco de dados MySQL é configurada via arquivo .editorconfig, onde você deve definir os parâmetros:
- host
- database
- user
- password

Estes parâmetros são lidos automaticamente pela aplicação no momento da execução.

### Criação Automática da Tabela e Usuário Administrador
Ao executar a aplicação pela primeira vez, o sistema cria automaticamente as tabelas necessárias no banco, caso ainda não existam.
Além disso, um usuário administrador padrão é criado automaticamente com as seguintes credenciais:
- Usuário: ```admin```
- Senha: ```123```
- Permissão: administrador (campo **bl_adm** = True)

Recomenda-se alterar esta senha após o primeiro acesso para garantir a segurança.

### Executando a Aplicação
Instale as dependências necessárias:
```
pip install -r requirements.txt
```
Execute o arquivo principal:
```
python main.py
```
A aplicação iniciará com a interface de login e estará pronta para uso.

## 🛠️ Tecnologias utilizadas #

Para o desenvolvimento desse projeto foram utilizadas as seguintes tecnologias:

* Python;
* PyQt5;
* QtDesigner;
* MySQL.
