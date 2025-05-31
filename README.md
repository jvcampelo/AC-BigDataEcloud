# Projeto Flask

Este é um projeto Flask com uma estrutura organizada incluindo models, controllers, config e database.

## Estrutura do Projeto

```
.
├── app/
│   ├── __init__.py
│   ├── config/
│   │   └── config.py
│   ├── controllers/
│   │   └── user_controller.py
│   └── models/
│       └── user.py
├── requirements.txt
├── run.py
└── README.md
```

## Instalação

1. Crie um ambiente virtual:
```bash
python -m venv venv
```

2. Ative o ambiente virtual:
- Windows:
```bash
venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
```
SECRET_KEY=sua-chave-secreta
DATABASE_URL=sqlite:///app.db
```

5. Inicialize o banco de dados:
```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

## Executando o projeto

Para iniciar o servidor Flask, execute:
```bash
python run.py
```

O servidor estará disponível em `http://localhost:5000`

## Endpoints da API

### Usuários
- GET `/api/users/` - Lista todos os usuários
- GET `/api/users/<id>` - Obtém um usuário específico
- POST `/api/users/` - Cria um novo usuário 