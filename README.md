# 📞 Inovador Blogspot - Flask

Um aplicativo web de **agenda telefônica** desenvolvido com **Flask**, **Flask-WTF**, **Flask-Login** e **Flask-SQLAlchemy**.  
Permite **adicionar, editar, visualizar e excluir contatos** de forma simples e intuitiva.

---

## 🚀 Tecnologias utilizadas

- **Flask** – Framework web principal  
- **Flask-WTF** – Criação e validação de formulários  
- **Flask-SQLAlchemy** – ORM para manipulação do banco de dados  
- **Flask-Login** – Autenticação de usuários  
- **Python-Dotenv** – Gerenciamento de variáveis de ambiente  
- **Email-Validator** – Validação de emails

---

## 🛠️ Instalação e execução

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/caio-dev-py/app.git
cd app
```

### 2️⃣ Instalar as dependências com Poetry
```bash
poetry install
```

### 3️⃣ Criar o arquivo `.env`
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```bash
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=sua_chave_secreta
SQLALCHEMY_DATABASE_URI=sqlite:///contatos.db
```

### 4️⃣ Rodar o servidor Flask
```bash
poetry run flask run
```

---

## 🧱 Estrutura do projeto

```
src/
 └── app/
      ├── __init__.py
      ├── models.py
      ├── routes.py
      ├── forms.py
      ├── templates/
      └── static/
```

---

## 👤 Autor

**Caio Daniel Araujo (caio-dev-py)**  
📧 [caio.dev.araujo@gmail.com](mailto:caio.dev.araujo@gmail.com)  
💻 [GitHub](https://github.com/caio-dev-py)

---

## 📝 Licença

Este projeto é distribuído sob a licença **MIT**.  
Sinta-se livre para usar, modificar e compartilhar.
