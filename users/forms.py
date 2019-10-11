import re
from django import forms
from django.contrib.auth.models import User


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.~?{}]+@\w+\.\w+)\"?")
    return re.match(pattern,email)

class Porfile_UpdateFrom(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=50,required=False)
    last_name = forms.CharField(label='Last Name',max_length=50,required=False)
    org = forms.CharField(label='Organization',max_length=128,required=False)
    telephone = forms.CharField(label='Telephone',max_length=11,required=False)


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("你的用户名太短！")
        elif len(username) > 50:
            raise forms.ValidationError("你的用户名太长！")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("用户名已存在，请重新输入！")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("你的邮箱已存在！")
        else:
            raise forms.ValidationError("请输入有效电子邮件。")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("该密码短。")
        elif len(password1) >50:
            raise forms.ValidationError("该密码太长！")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不符合。 请再次输入。")
        return password2

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='password',widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if email_check(username):
            filter_result = User.objects.filter(email__exact=username)
            if not filter_result:
                raise forms.ValidationError("该电子邮件不存在。")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if not filter_result:
                raise forms.ValidationError("该用户名不存在。")

        return username

class PwdChangeFrom(forms.Form):
    old_pwd = forms.CharField(label='oldpwd',widget=forms.PasswordInput)
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput)

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError('密码太短。')

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不符合。 请再次输入。")

        return password2