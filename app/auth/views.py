from flask import redirect, url_for, flash
from flask import Blueprint, render_template
from flask_login import login_user, logout_user, login_required

from app.auth.forms import LoginForm, RegisterForm
from app.auth.modles import User
from app import login_manager

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        current_user = User.query.filter_by(email=login_form.email.data).first()
        if current_user and current_user.verify_password(login_form.password.data):
            login_user(current_user)
            return redirect(url_for('home.index'))
        flash('帐户名或密码错误')
    return render_template('login.html', login_form=login_form)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        pass
    return render_template('register.html', register_form=register_form)


@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('登出成功')
    return redirect(url_for('auth.login'))
