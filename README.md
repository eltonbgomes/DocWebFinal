# DocWeb

Aplica��o para armazenar informa��es de usu�rios e mostra-los atrav�s de autentifica��o.

A aplica��o utiliza o framework Django 3.0.2 e o interpretador Python 3.8.1, ambos em suas vers�es atuais.

1) Fa�a o download deste reposit�rio em uma nova pasta;
2) Instale o Python 3.8.1;
3) Abra o terminal e instale o virtualenv utilizando o comando "pip install virtualenv";
4) Na nova pasta onde est�o os arquivos do reposit�rio, crie um ambiente virtual atrav�s do comando "python -m venv venv";
5) Ative o ambiente virtual;
6) Com o ambiente virtual instalado, abra o arquivo "requirements-dev" disponivel no repositorio
e intale as bibliotecas requiridas;
7)Fa�a as migra��es e cria o banco de dados: "python manage.py makemigrations" e "python manage.py migrate"
8) Digite o comando "python manage.py runserver" para ativar o servidor local;
9) Abra o navegador e digite "http://localhost:8000/".

Note: O acesso ao sistema � criado pelo terminal atrav�s do comando "python manage.py createsuperuser"
Note2: Um exemplo do AppWeb criado encontra-se disponivel em http://docweb1.herokuapp.com/, o acesso ao
sistema � possivel nesse site atrav�s de:
usuario: admin
senha: but&d543
