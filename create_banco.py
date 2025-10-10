from src.app import create_app
from src.app import db

app = create_app()

with app.app_context():
    db.create_all()
    print ("Banco de dados criado com sucesso.")