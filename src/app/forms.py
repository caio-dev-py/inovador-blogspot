from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class CadastroForm(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired(message="O nome não pode estar vazio.")])
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                             Length(min=8, message="A senha deve ter ao menos 8 caracteres.")])
    conf_senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                             Length(min=8, message="A senha deve ter ao menos 8 caracteres."),
                                             EqualTo("senha", message="As senhas não coincidem.")])
    cadastrar = SubmitField("Cadastrar")

class LoginForm(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(message="O e-mail não pode estar vazio."),
                                              Email(message="E-mail inválido.")])
    senha = PasswordField("Senha", validators=[DataRequired(message="A senha não pode estar vazia."),
                                               Length(min=8, message="A senha deve ter ao menos 8 caracteres.")])
    login = SubmitField("Login")

class PostForm(FlaskForm):
    titulo = StringField("Título", validators=[DataRequired(message="O título deve ser preenchido.")])
    conteudo = TextAreaField("Conteúdo", validators=[DataRequired(message="Conteúdo não pode estar vazio.")])
    postar = SubmitField("Postar")

class DeletarForm(FlaskForm):
    deletar = SubmitField("Deletar")