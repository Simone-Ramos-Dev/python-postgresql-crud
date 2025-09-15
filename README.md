# Aplicação de CRUD em Python com Flask e PostgreSQL
Este projeto é uma API simples em Python que demonstra operações CRUD (Criar, Ler, Atualizar, Excluir) em um banco de dados PostgreSQL. Ele usa o framework Flask para o servidor web e a biblioteca Psycopg2 para gerenciar as interações com o banco de dados.

## ⚙️ Tecnologias Utilizadas
Python 3.x: Linguagem de programação principal.

Flask: Um micro framework web leve e versátil.

Psycopg2: Adaptador oficial para banco de dados PostgreSQL.

python-dotenv: Para carregar variáveis de ambiente de forma segura a partir de um arquivo .env.

## 📂 Estrutura do Projeto
app.py: O coração da aplicação. Contém as rotas da API e a lógica para lidar com as requisições HTTP (GET, POST, PUT, DELETE).

database.py: Módulo responsável por estabelecer e gerenciar a conexão com o banco de dados PostgreSQL.

models.py: Define os modelos de dados e a estrutura das tabelas que serão criadas no banco.

create_tables.py: Script de uso único para criar as tabelas do banco de dados com base nos modelos definidos.

.env: Arquivo para armazenar variáveis de ambiente sensíveis, como credenciais de banco de dados. (Este arquivo não deve ser enviado para o GitHub).

requirements.txt: Lista todas as dependências do projeto, facilitando a instalação.

.gitignore: Define quais arquivos e pastas o Git deve ignorar (ex: venv/, .env, __pycache__/).

## 🚀 Como Rodar o Projeto
Siga estes passos para configurar e executar o projeto em sua máquina local.

Pré-requisitos
Certifique-se de ter o Python 3 e o PostgreSQL instalados.

1. Clonar o Repositório
Bash

git clone https://github.com/Simone-Ramos-Dev/python-postgresql-crud
cd seu-repositorio
2. Configurar o Ambiente Virtual
É uma boa prática usar um ambiente virtual para gerenciar as dependências do projeto.

Bash

python -m venv venv
Ative o ambiente virtual:

No Windows: venv\Scripts\activate

No macOS/Linux: source venv/bin/activate

3. Instalar as Dependências
Instale todas as bibliotecas necessárias listadas no arquivo requirements.txt.

Bash

pip install -r requirements.txt
4. Configurar o Banco de Dados
Crie um banco de dados PostgreSQL para o projeto.

Crie um arquivo .env na raiz do projeto com as suas credenciais.

Snippet de código

DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=seu_host
DB_PORT=5432
DB_NAME=seu_banco
Execute o script para criar as tabelas.

Bash

python create_tables.py
5. Executar a Aplicação
Com o ambiente configurado, você pode iniciar o servidor.

Bash

python app.py
A API estará rodando em http://127.0.0.1:5000.

📝 Endpoints da API
Você pode testar a API usando ferramentas como o Postman ou Insomnia.

Método	Endpoint	Descrição
POST	/api/items	Cria um novo item no banco de dados.
GET	/api/items	Retorna todos os itens.
GET	/api/items/<id>	Retorna um item específico pelo ID.
PUT	/api/items/<id>	Atualiza os dados de um item existente.
DELETE	/api/items/<id>	Exclui um item do banco de dados.

Exportar para as Planilhas
🤝 Contribuições
Contribuições são bem-vindas! Se você encontrou um bug ou tem uma ideia de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.

📄 Licença
Este projeto está licenciado sob a Licença MIT.
