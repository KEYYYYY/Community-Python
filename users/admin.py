from django.contrib import admin

from .models import BlogArticle


class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_time')
    list_filter = ('title', 'publish_time')
    search_fields = ('title', 'body')


admin.site.register(BlogArticle, BlogArticleAdmin)
