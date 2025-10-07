from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    senha = db.Column(db.String(), nullable=False)
    posts = db.relationship("Postagens", backref="usuario", lazy=True)

class Postagens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    titulo = db.Column(db.String(150), nullable=False)
    conteudo = db.Column(db.String(150000), nullable=False)
    data_postagem = db.Column(db.DateTime, default=datetime.now())