from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[
        DataRequired(message='这是必填字段'),
        Email(message='请输入正确的邮箱')
    ])
    password = PasswordField('密码', validators=[
        DataRequired(message='这是必填字段'),
        Length(8, 32, message='请输入8-32位的密码')
    ])
    submit = SubmitField('登录')
