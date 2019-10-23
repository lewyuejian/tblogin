from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password

from .forms import LoginForm,RegisterForm,Porfile_UpdateFrom,PwdChangeFrom
from .models import UserProfile


#注册
def RegisterView(request):
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password2']
            user = User.objects.create_user(username=username,email=email,password=password)
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('users:login'))

    else:
        form = RegisterForm()
    return render(request,'users/registration.html',{'form':form})

#登录
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None and user.is_active:
                auth.login(request,user)
                return HttpResponseRedirect(reverse("users:profile",args=[user.id]))

            else:
                #登录失败
                return render(request,'users/login.html',{'form':form,'message':'密码不正确，请重新输入密码！'})
    else:
        form = LoginForm()
    return render(request,'users/login.html',{'form':form})

#个人信息
@login_required                     #判断用户是否登录
def Profile(request,pk):
    user = get_object_or_404(User,pk=pk)
    return render(request,'users/profile.html',{'user':user})

#更新用户信息
@login_required
def profile_update(request,pk):
    user = get_object_or_404(User,pk=pk)
    user_profile = get_object_or_404(UserProfile, user=user)

    if request.method == 'POST':
        form = Porfile_UpdateFrom(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()

            user_profile.org = form.cleaned_data['org']
            user_profile.telephone = form.cleaned_data['telephone']
            user_profile.save()

            return HttpResponseRedirect(reverse('users:profile',args=[user.id]))
    else:
        file_profile = {
            'first_name':user.first_name,'last_name':user.last_name,
            'org':user_profile.org,'telephone':user_profile.telephone,
        }
        form = Porfile_UpdateFrom(file_profile)
    return render(request,'users/profile_update.html',{'form':form, 'user': user})

#密码修改
@login_required
def pwd_change(request,pk):
    user = get_object_or_404(User,pk=pk)

    if request.method == 'POST':
        form = PwdChangeFrom(request.POST)
        if form.is_valid():
            old_pwd = form.cleaned_data['old_pwd']
            password = form.cleaned_data['password2']

            # 校验密码 格式：check_password("123456","pbkdf2_sha25615000MAjic3nDGFoi$qbclz+peplspCbRF6uoPZZ42aJIIkMpGt6lQ+Iq8nfQ=")
            if check_password(old_pwd,user.password):
                user.password = make_password(password)         #密码加密
                user.save()
                return HttpResponseRedirect(reverse('users:login'))

            else:
                return render(request,"users/pwdchange.html",{'form':form,'msg':'旧密码不正确!'})
    else:
        form = PwdChangeFrom()
    return render(request,'users/pwdchange.html',{'form':form, 'user': user})


def index(request):
    return render(request,'index.html')

def tbl_setting(request):
    return render(request, 'users/tbl_setting.html')


#退出
def LogoutView(request):
    return render(request,'users/logout.html')

