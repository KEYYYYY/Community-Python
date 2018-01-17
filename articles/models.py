from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class ArticleColumn(models.Model):
    user = models.ForeignKey(User, related_name='columns', verbose_name='用户')
    name = models.CharField(max_length=64, unique=True, verbose_name='名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    user = models.ForeignKey(User, related_name='articles', verbose_name='作者')
    column = models.ForeignKey(
        ArticleColumn,
        related_name='articles',
        verbose_name='所属栏目'
    )
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(null=True, blank=True, verbose_name='正文')
    content_html = models.TextField(
        null=True,
        blank=True,
        verbose_name='正文MarkDown'
    )
    images = models
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',)

    def __str__(self):
        return self.title


class ArticleImage(models.Model):
    article = models.ForeignKey(
        'Article', blank=True, related_name='images', verbose_name='插图')

    class Meta:
        verbose_name = '插图'
        verbose_name_plural = verbose_name
