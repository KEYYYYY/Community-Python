from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Length, DataRequired
from flask_pagedown.fields import PageDownField


class EditProfileForm(FlaskForm):
    username = StringField('用户名', validators=[
        Length(3, 32, message='用户名必须在3-32位之间'),
    ])
    location = StringField('地址')
    about_me = TextAreaField('自我介绍')
    submit = SubmitField('保存')


class ArticleForm(FlaskForm):
    title = StringField('标题', validators=[
        DataRequired(message='这是必填字段'),
        Length(0, 32, message='题目要求在64个字以内')
    ])
    content = PageDownField('正文')
    submit = SubmitField('发表')
