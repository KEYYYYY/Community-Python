from django.conf.urls import url
from django.contrib.auth import views

from accounts.views import UserRegiserView, UserProfileView
from accounts.forms import LoginForm, UserPasswordChangeForm

urlpatterns = [
    url(r'^login/$', views.login, {
        'template_name': 'accounts/login.html',
        'authentication_form': LoginForm,
    }, name='login'),
    url(r'^logout/$', views.logout, {
        'next_page': '/accounts/login/',
    }, name='logout'),
    url(r'^password-change/$', views.password_change, {
        'template_name': 'accounts/password-change.html',
        'post_change_redirect': '/accounts/login',
        'password_change_form': UserPasswordChangeForm,
    }, name='password_change'),
    url(r'^regiser/$', UserRegiserView.as_view(), name='register'),
    url(r'^profile/$', UserProfileView.as_view(), name='profile'),
]
