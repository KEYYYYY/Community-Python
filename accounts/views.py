from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View

from accounts.forms import RegiserForm, UserProfileForm
from accounts.models import UserProfile


class UserRegiserView(View):
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


class UserProfileView(View):
    def get(self, request):
        profile_form = UserProfileForm(instance=request.user.user_profile)
        return render(request, 'accounts/profile.html', {
            'profile_form': profile_form,
        })

    def post(self, request):
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            user_profile = request.user.user_profile
            user_profile.phone = profile_form.cleaned_data.get('phone')
            user_profile.save()
        return render(request, 'accounts/profile.html', {
            'profile_form': profile_form,
        })
