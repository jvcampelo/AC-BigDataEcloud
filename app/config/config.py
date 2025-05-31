import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configurações do Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-padrao'
    
    # Configurações do Banco de Dados
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:123456789@localhost:3306/ac_bigdata'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Configurações adicionais
    DEBUG = True 