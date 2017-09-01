from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, Regexp


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[
        Length(3, 32, message='用户名必须在3-32位之间'),
        Regexp(r'[0-9a-zA-Z_@.]+', message='用户名只能由字母、数字、下划线、.、@组成'),
    ])
    location = StringField('地址')
    about_me = TextAreaField('自我介绍')
    submit = SubmitField('保存')
