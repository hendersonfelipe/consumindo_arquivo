## Projeto de Consumindo Arquivo para Programação Para Internet II

No que consite este projeto:
- Fazer upload de arquivos ".xlsx" o arquivo utilizado no exemplo foi o "data.xlsx"
- Realizar carga de dados do arquivos para o Banco de Dados.
- Transformar coluna "nascimento" para data.
- Fazer consulta retornando mulheres de Meeren.
- Receber o sexo (M ou F) como parâmetro, filtrar e retornar a lista
de pessoas, ordenada por idade.

## Configurando o ambiente para executar a api.
Faça o download deste repositório:
```
$ git clone git@github.com:hendersonfelipe/consumindo_arquivo.git
```

Crie um ambiente virtual e instale a bibliotecas disponíveis no 
arquivo requirements.txt

Entre na pasta criada e inicie um ambiente virtual:
```
$ cd consumindo_arquivo
$ python -m venv venv
```

Depois vamos ativá-lo com o seguinte comando:
```
$ .\venv\Scripts\Activate
```

Depois de ativado, instale as bibliotecas necessárias para executar o projeto:
```
 (venv)$ pip install -r requeriments.txt
```

Para fazermos o primeiro acesso e poder configurar a aplicação, vamos executar o comando 
'migrate' para gerar o banco de dados padrão do Django(SQLite). E depois criar o superusuário:
```
(venv)$ python manage.py migrate
(venv)$ python manage.py createsuperuser
Apelido/Usuário: admin
E-mail: admin@mail.com
Password: 
Password (again):
```

Agora devemos iniciar o servidor usando o comando:
```
(venv)$ python manage.py runserver
```

Agora vamos acessar o seguinte endereço:
[http://localhost:8000/](http://localhost:8000/)

Ou você pode ter acesso a admin do Django:
[http://localhost:8000/admin](http://localhost:8000/admin)

```
Tú é um corno kkkkkkk
```
