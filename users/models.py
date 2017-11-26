from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class BlogArticle(models.Model):
    title = models.CharField(max_length=128, null=False, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    author = models.ForeignKey(User, related_name='posts', verbose_name='作者')
    publish_time = models.DateTimeField(
        default=datetime.now, verbose_name='发表时间'
    )

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
