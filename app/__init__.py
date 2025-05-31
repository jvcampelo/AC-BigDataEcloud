from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restx import Api
from app.config.config import Config

db = SQLAlchemy()
migrate = Migrate()
api = Api(
    title='API de Matrículas',
    version='1.0',
    description='API para gerenciamento de matrículas de alunos',
    doc='/docs'
)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicialização das extensões
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    api.init_app(app)

    # Importa e registra os namespaces
    from app.controllers.matricula_controller import ns
    api.add_namespace(ns)

    # Cria as tabelas do banco de dados
    with app.app_context():
        db.create_all()

    return app 