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
        default='保密',
        max_length=256,
        verbose_name='地址'
    )
    about_me = models.TextField(
        null=True,
        blank=True,
        default='这个人很懒，什么都没有说',
        verbose_name='自我介绍'
    )
    avatar = models.ImageField(
        upload_to='avatars',
        default='avatars/default.jpg',
        null=True,
        blank=True,
        verbose_name='头像'
    )
    followers = models.ManyToManyField(
        'UserProfile',
        related_name='followeds',
        verbose_name='关注他的人'
    )

    def is_following(self, user_profile_id):
        user_profile = UserProfile.objects.get(id=user_profile_id)
        if user_profile in self.followeds.all():
            return True
        return False

    def following(self, user_id):
        user_profile = UserProfile.objects.get(id=user_id)
        user_profile.followers.add(self)
        user_profile.save()

    def unfollowing(self, user_id):
        user_profile = UserProfile.objects.get(id=user_id)
        user_profile.followers.remove(self)
        user_profile.save()

    def get_following_count(self):
        return self.followeds.count()

    def get_followers_count(self):
        return self.followers.count()

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
