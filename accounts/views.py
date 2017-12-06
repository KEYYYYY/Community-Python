from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.generic.base import View

from accounts.forms import AvatarUploadForm, RegiserForm, UserProfileForm
from accounts.models import UserProfile


class UserRegiserView(View):
    """
    用户注册视图
    """

    def get(self, request):
        regiser_form = RegiserForm()
        return render(request, 'accounts/register.html', {
            'form': regiser_form,
        })

    def post(self, request):
        regiser_form = RegiserForm(request.POST)
        if regiser_form.is_valid():
            user = regiser_form.save()
            user_profile = UserProfile(
                user=user,
                phone=regiser_form.cleaned_data.get('phone')
            )
            user_profile.save()
            return redirect(reverse('accounts:login'))
        return render(request, 'accounts/register.html', {
            'form': regiser_form,
        })


class UserProfileEditView(LoginRequiredMixin, View):
    """
    用户编辑个人信息页面
    """
    login_url = '/accounts/login/'

    def get(self, request):
        profile_form = UserProfileForm(instance=request.user.user_profile)
        return render(request, 'accounts/profile-edit.html', {
            'profile_form': profile_form,
        })

    def post(self, request):
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            user_profile = request.user.user_profile
            user_profile.location = profile_form.cleaned_data.get('location')
            user_profile.phone = profile_form.cleaned_data.get('phone')
            user_profile.save()
        return render(request, 'accounts/profile.html', {
            'profile_form': profile_form,
        })


class UserProfileView(View):
    """
    用户信息页视图
    """

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        # 如果不做匿名用户判断，匿名用户没有user_profile会把服务器挂掉
        if request.user.is_authenticated():
            is_following = request.user.user_profile.is_following(
                user.user_profile.id)
            return render(request, 'accounts/profile.html', {
                'user': user,
                'is_following': is_following,
            })
        else:
            return render(request, 'accounts/profile.html', {
                'user': user,
            })

    def post(self, request, user_id):
        # 得到当前查看的用户
        user = get_object_or_404(User, id=user_id)
        # 如果已经关注过则取消关注
        if request.user.user_profile in user.user_profile.followers.all():
            request.user.user_profile.unfollowing(user.user_profile.id)
            return JsonResponse({'status': 'ok'})
        # 未关注则关注
        request.user.user_profile.following(user.user_profile.id)
        return JsonResponse({'status': 'ok'})


class AvatarUploadView(View):
    """
    修改头像视图
    """

    def post(self, request):
        avatar_upload_form = AvatarUploadForm(request.POST, request.FILES)
        if avatar_upload_form.is_valid():
            avatar = avatar_upload_form.cleaned_data.get('avatar')
            user_profile = request.user.user_profile
            user_profile.avatar = avatar
            user_profile.save()
        return redirect(reverse('accounts:profile', user_id=request.user.id))
