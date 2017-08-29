from flask import Blueprint, render_template

from app.auth.forms import LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        pass
    return render_template('login.html', login_form=login_form)
