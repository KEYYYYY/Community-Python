from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    用户信息模型
    """
    user = models.OneToOneField(
        User,
        related_name='user_profile',
        verbose_name='用户'
    )
    phone = models.CharField(
        null=True,
        blank=True,
        max_length=11,
        verbose_name='电话'
    )
    location = models.CharField(
        null=True,
        blank=True,
        max_length=256,
        verbose_name='地址'
    )
    about_me = models.TextField(
        null=True,
        blank=True,
        verbose_name='自我介绍'
    )
    avatar = models.ImageField(
        upload_to='avatars',
        default='avatars/default.jpg',
        null=True,
        blank=True,
        verbose_name='头像'
    )

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
