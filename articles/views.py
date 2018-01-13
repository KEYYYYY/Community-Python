from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
import markdown

from articles.forms import ArticleForm
from articles.models import Article


class IndexView(ListView):
    """
    首页视图
    """
    model = Article
    template_name = 'articles/index.html'
    context_object_name = 'articles'

    def get(self, request):
        return render(request, 'base.html')


class EditArticle(View):
    """
    发布文章视图
    """

    def get(self, request):
        article_form = ArticleForm()
        return render(request, 'articles/edit-article.html', {
            'article_form': article_form,
        })

    def post(self, request):
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 将文章内容转化为MarkDown格式
            article.content_html = markdown.markdown(
                article.content, extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                    'markdown.extensions.toc',
                ]
            )
            article.user = request.user
            article.save()
        return redirect(reverse('articles:index'))


class ModifyArticleView(View):
    """
    修改文章视图
    """
    pass


class ArticleDetailView(DetailView):
    """
    查看文章详情视图
    """

    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        return render(request, 'articles/article-detail.html', {
            'article': article
        })
