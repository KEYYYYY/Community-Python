import re

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserCreationForm)

from accounts.models import UserProfile


class LoginForm(AuthenticationForm):
    """
    用户登陆表单
    """
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(
        Submit('login', '登陆', css_class='btn-primary btn-block')
    )


class RegiserForm(UserCreationForm):
    """
    用户注册表单
    """
    password1 = forms.CharField(
        label='密码',
        strip=False,
        widget=forms.PasswordInput,
        help_text='请输入至少8位密码，并且不能太简单'
    )
    phone = forms.CharField(
        label='手机号',
        help_text='请输入11位手机号',
        max_length=11,
        min_length=11
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\d+', phone):
            return phone
        raise forms.ValidationError('请填写正确的手机号')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(
        Submit('login', '注册', css_class='btn-primary btn-block')
    )


class UserPasswordChangeForm(PasswordChangeForm):
    """
    用户更改密码表单
    """
    new_password1 = forms.CharField(
        label='密码',
        strip=False,
        widget=forms.PasswordInput,
        help_text='请输入至少8位密码，并且不能太简单'
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(
        Submit('login', '修改密码', css_class='btn-primary btn-block')
    )


class UserProfileForm(forms.ModelForm):
    """
    用户个人信息表单
    """
    class Meta:
        model = UserProfile
        exclude = ('user', 'avatar', 'followers')

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if re.match(r'\d{11,11}', phone):
            return phone
        raise forms.ValidationError('请填写正确的手机号')

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(
        Submit('login', '更新', css_class='btn-primary btn-block')
    )
