from django import forms
from django.contrib.auth.models import User
import re


def email_check(email):
    pattern = re.compile(r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?")
    return re.match(pattern, email)

class RegistrationForm(forms.Form):

    username = forms.CharField(label='Username', max_length=50)
    email = forms.EmailField(label='Email',)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    # Use clean methods to define custom validation rules

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("您的用户名必须至少包含6个字符。")
        elif len(username) > 50:
            raise forms.ValidationError("您的用户名太长。")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("您的用户名已经存在。")

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email_check(email):
            filter_result = User.objects.filter(email__exact=email)
            if len(filter_result) > 0:
                raise forms.ValidationError("您的电子邮件已经存在！")
        else:
            raise forms.ValidationError("请输入有效电子邮件！")

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("您输入的密码太短！")
        elif len(password1) > 20:
            raise forms.ValidationError("您输入的密码太长！")

        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不符合！请再次输入！")

        return password2


class LoginForm(forms.Form):

  username = forms.CharField(label='Username', max_length=50)
  password = forms.CharField(label='Password', widget=forms.PasswordInput)

  # Use clean methods to define custom validation rules
  def clean_username(self):
    username = self.cleaned_data.get('username')

    if email_check(username):
      filter_result = User.objects.filter(email__exact=username)
      if not filter_result:
        raise forms.ValidationError("电子邮件不存在！")
    else:
      filter_result = User.objects.filter(username__exact=username)
      if not filter_result:
        raise forms.ValidationError("用户名不存在！请先注册！")

    return username

class ProfileForm(forms.Form):

    first_name=forms.CharField(label='First Name', max_length=50,
                                required=False)
    last_name=forms.CharField(label='Last Name', max_length=50,
                               required=False)


