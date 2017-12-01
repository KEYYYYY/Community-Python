from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='user_profile',
        verbose_name='用户'
    )
    phone = models.CharField(max_length=11, verbose_name='电话')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
