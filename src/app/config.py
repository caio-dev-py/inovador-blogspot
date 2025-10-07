import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # CONFIGURAÇÃO DA CHAVE SECRETA
    SECRET_KEY = os.getenv("SECRET_KEY")

    # CONFIGURAÇÃO DO BANCO DE DADOS
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, "database.db")}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False