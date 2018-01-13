from django.forms import ModelForm
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

from articles.models import Article


class ArticleForm(ModelForm):
    """
    文章表单
    """
    class Meta:
        model = Article
        fields = ('column', 'title', 'content')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(
        Submit('submit', '发布', css_class='btn-primary btn-block')
    )
