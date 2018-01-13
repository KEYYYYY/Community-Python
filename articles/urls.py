from django.conf.urls import url

from articles.views import IndexView, EditArticle, ArticleDetailView

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^article-edit/$', EditArticle.as_view(), name='edit_article'),
    url(r'^article-detail/(?P<article_id>\d+)$',
        ArticleDetailView.as_view(), name='detail_article'),
]
