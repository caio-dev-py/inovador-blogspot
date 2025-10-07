from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from src.app.models import Postagens, Usuarios, db
from src.app.forms import PostForm, DeletarForm

user_route = Blueprint("user", __name__)

@user_route.route("/posts", methods=["GET", "POST"])
@login_required
def posts():
    posts = Postagens.query.all()
    usuarios = Usuarios.query.all()
    return render_template("posts.html", posts=posts, usuarios=usuarios)

@user_route.route("/perfil", methods=["GET", "POST"])
@login_required
def perfil():
    form = DeletarForm()
    perfil_posts = Postagens.query.filter_by(id_usuario=current_user.id).all()
    return render_template("perfil_posts.html", perfil_posts=perfil_posts, form=form)

@user_route.route("/postar", methods=["GET", "POST"])
@login_required
def postar():
    form = PostForm()

    if form.validate_on_submit():
        titulo = form.titulo.data
        conteudo = form.conteudo.data
        
        post = Postagens(id_usuario=current_user.id, titulo=titulo, conteudo=conteudo)

        db.session.add(post)
        db.session.commit()

        flash ("Postagem feita com sucesso.", "success")
        return redirect(url_for("user.posts"))

    return render_template("form_post.html", form=form, action="/postar")


@user_route.route("/editar", methods=["GET", "POST"])
@login_required
def editar_sem_id():
    return redirect(url_for("user.perfil"))

@user_route.route("/editar/<int:id_post>", methods=["GET", "POST"])
@login_required
def editar(id_post):
    post = Postagens.query.get_or_404(id_post)
    form = PostForm(obj=post)

    if form.validate_on_submit():
        post.titulo = form.titulo.data
        post.conteudo = form.conteudo.data

        db.session.commit()
        flash("Post atualizado com sucesso!", "success")
        return redirect(url_for("user.perfil"))

    return render_template("editar_post.html", form=form, action=url_for("user.editar", id_post=id_post), post=post)

@user_route.route("/deletar/<int:id_post>", methods=["POST"])
@login_required
def deletar(id_post):
    form = DeletarForm()

    if form.validate_on_submit():
        post = Postagens.query.filter_by(id=id_post).first()
        
        if post:
            db.session.delete(post)
            db.session.commit()

            flash ("Post deletado.", "warning")
            return redirect(url_for("user.perfil"))
        flash ("ID não encontrado.", "danger")
        return redirect(url_for("user.perfil"))