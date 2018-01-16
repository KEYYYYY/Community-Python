from django.conf.urls import url

from articles.views import (AddColumnView, ArticleDetailView, EditArticle,
                            IndexView, upload_image)

urlpatterns = [
    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^article-edit/$', EditArticle.as_view(), name='edit_article'),
    url(r'^add-column/$', AddColumnView.as_view(), name='add_column'),
    url(r'^article-detail/(?P<article_id>\d+)$',
        ArticleDetailView.as_view(), name='detail_article'),
    url(r'^image-upload/$', upload_image, name='image_upload')
]
