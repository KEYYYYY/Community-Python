import xadmin
from articles.models import ArticleColumn, Article


class ArticleColumnAdmin:
    list_display = ['user', 'name', 'add_time']
    search_fields = ['name', 'add_time']
    list_filter = ['user', 'name', 'add_time']


class ArticleAdmin:
    list_display = ['user', 'column', 'title', 'add_time']
    search_fields = ['title', 'content', 'add_time']
    list_filter = ['user', 'column', 'title', 'add_time']


xadmin.site.register(ArticleColumn, ArticleColumnAdmin)
xadmin.site.register(Article, ArticleAdmin)
