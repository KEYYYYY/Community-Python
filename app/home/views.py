from flask import Blueprint, render_template, abort, flash, redirect, url_for
from flask import request
from flask_login import login_required, current_user

from app.auth.modles import User
from app.home.models import Article, Comment
from app.home.forms import EditProfileForm, ArticleForm, CommentForm
from app import db

home = Blueprint('home', __name__)


@home.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Article.query.order_by(Article.publish_time.desc()).paginate(
        page,
        per_page=2
    )
    articles = pagination.items
    return render_template(
        'index.html',
        articles=articles,
        pagination=pagination
    )


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
    return render_template(
        'edit-profile.html',
        edit_profile_form=edit_profile_form
    )


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
        article.change_content()
        db.session.add(article)
        db.session.commit()
        flash('发表成功')
        return redirect(url_for('home.index'))
    return render_template('edit-article.html', article_form=article_form)


@home.route('/user/<user_id>/profile/')
def profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('profile.html', user=user)


@home.route('/modify_article/<article_id>/', methods=['GET', 'POST'])
@login_required
def modify_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author != current_user:
        abort(403)
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        article.title = article_form.title.data
        article.content = article_form.content.data
        article.change_content()
        db.session.add(article)
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('home.index'))
    article_form.title.data = article.title
    article_form.content.data = article.content
    return render_template('modify-article.html', article_form=article_form)


@home.route('/remove_article/<article_id>/')
@login_required
def remove_article(article_id):
    article = Article.query.get_or_404(article_id)
    if article.author != current_user:
        abort(403)
    db.session.delete(article)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('home.index'))


@home.route('/follow/<user_id>/')
@login_required
def follow(user_id):
    user = User.query.get_or_404(user_id)
    current_user.follow(user)
    flash('关注成功')
    return redirect(url_for('home.profile', user_id=user_id))


@home.route('/unfollow/<user_id>/')
@login_required
def unfollow(user_id):
    user = User.query.get_or_404(user_id)
    current_user.unfollow(user)
    flash('取消关注成功')
    return redirect(url_for('home.profile', user_id=user_id))


@home.route('/article/<article_id>/', methods=['GET', 'POST'])
@login_required
def article_detail_and_comment(article_id):
    article = Article.query.get_or_404(article_id)
    # 浏览量+1
    article.page_view += 1
    db.session.add(article)
    db.session.commit()
    comment_form = CommentForm()
    # 对评论先分页
    page = request.args.get('page', 1, type=int)
    pagination = article.comments.order_by(Comment.timestamp.desc()).paginate(
        page,
        per_page=3
    )
    comments = pagination.items
    # 提交评论
    if comment_form.validate_on_submit():
        comment = Comment(
            user=current_user._get_current_object(),
            article=article,
            content=comment_form.content.data
        )
        comment.change_content()
        db.session.add(comment)
        db.session.commit()
        flash('评论成功')
        return redirect(
            url_for(
                'home.article_detail_and_comment',
                article_id=article_id
            )
        )
    return render_template(
        'article-detail.html',
        article=article,
        comment_form=comment_form,
        comments=comments,
        pagination=pagination
    )
