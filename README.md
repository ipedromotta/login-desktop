<h1 align="center">
<img src="https://github.com/ipedromotta/VueJS-Flask/blob/main/frontend/src/assets/logo-python.png" width="50"><br>Sistema de login Python/MySQL
</h1>

## 📄 Sobre #

<p> 
Este é um sistema de login desktop que faz CRUD.<br>
Para desenvolver a interface do sistema foi utilizado a biblioteca PyQt5 com o QtDesigner.
</p>
<p>
Existe uma janela para a manipulação de dados diretamente da aplicação. Para ter acesso a essa tela basta criar um usuario com a coluna bl_adm como true.
</p>

### Configuração do projeto 

Instale todas as dependencias do projeto com o comando:
```
pip install -r requirements.txt
```
<p>
A estrutura de banco de dados já está pronta no arquivo db_login.sql. Execute este arquivo no MySQL Workbench para criar a estrutura. <br>
Caso tenha mexido na estrutura do banco basta passar os novos parametros no o arquivo .editorconfig.
</p>
<p>
Após fazer a configuração basta executar o arquivo main.py e a aplicação irá executar normalmente.
</p>

## 🛠️ Tecnologias utilizadas #

Para o desenvolvimento desse projeto foram utilizadas as seguintes tecnologias:

* Python;
* PyQt5;
* QtDesigner;
* MySQL.
