from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.auth.models import User


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


class RegisterForm(FlaskForm):
    email = StringField('邮箱', validators=[
        DataRequired(message='这是必填字段'),
        Email(message='请输入正确的邮箱')
    ])
    password = PasswordField('密码', validators=[
        DataRequired(message='这是必填字段'),
        Length(8, 32, message='请输入8-32位的密码'),
        EqualTo('password2', message='两次输入的密码不一致')
    ])
    password2 = PasswordField('重复密码', validators=[
        DataRequired(message='这是必填字段')
    ])
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经注册')


class ModifyPasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[
        DataRequired(message='这是必填字段'),
        Length(8, 32, message='请输入8-32位的密码')
    ])
    new_password = PasswordField('新密码', validators=[
        DataRequired(message='这是必填字段'),
        Length(8, 32, message='请输入8-32位的密码'),
        EqualTo('new_password2', message='两次输入的密码不一致')
    ])
    new_password2 = PasswordField('重复新密码', validators=[
        DataRequired(message='这是必填字段'),
        Length(8, 32, message='请输入8-32位的密码'),
    ])
    submit = SubmitField('确认修改')
