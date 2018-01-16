from django.forms import ModelForm

from articles.models import Article, ArticleColumn


class BaseForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class ArticleForm(BaseForm):
    """
    文章表单
    """

    class Meta:
        model = Article
        fields = ('column', 'title', 'content')


class ColumnForm(BaseForm):
    """
    栏目表单
    """

    class Meta:
        model = ArticleColumn
        fields = ('name',)
