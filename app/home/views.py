from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
from flask_login import login_required, current_user

from app.auth.modles import User
from app.home.models import Article
from app.home.forms import EditProfileForm, ArticleForm
from app import db

home = Blueprint('home', __name__)


@home.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.publish_time.desc()).paginate(
        page,
        per_page=3
    )
    articles = pagination.items
    return render_template('index.html', articles=articles, pagination=pagination)


@home.route('/user/<user_id>/edit_profile/', methods=['GET', 'POST'])
@login_required
def edit_profile(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user or user != current_user:
        abort(404)
    edit_profile_form = EditProfileForm()
    if edit_profile_form.validate_on_submit():
        username = edit_profile_form.username.data
        location = edit_profile_form.location.data
        about_me = edit_profile_form.about_me.data
        user.username = username
        user.location = location
        user.about_me = about_me
        db.session.add(user)
        db.session.commit()
        flash('修改信息成功')
        return redirect(url_for('home.index'))
    edit_profile_form.username.data = user.username
    edit_profile_form.location.data = user.location
    edit_profile_form.about_me.data = user.about_me
    return render_template('edit-profile.html', edit_profile_form=edit_profile_form)


@home.route('/edit_article/', methods=['GET', 'POST'])
@login_required
def edit_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article = Article(
            title=article_form.title.data,
            content=article_form.content.data,
            author=current_user
        )
        db.session.add(article)
        db.session.commit()
        flash('发表成功')
        return redirect(url_for('home.index'))
    return render_template('edit-article.html', article_form=article_form)


@home.route('/user/<user_id>/profile/')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)
