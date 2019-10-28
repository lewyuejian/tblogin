from django.urls import re_path,path

from . import views,viewsmaterial,viewstools,viewsreport

app_name = 'users'
urlpatterns = [

    re_path(r'register/$',views.RegisterView,name='register'),#注册
    re_path(r'login/$',views.LoginView,name='login'),#登录
    re_path(r'user/(?P<pk>\d+)/profile/$',views.Profile,name='profile'),#个人信息
    re_path(r'user/(?P<pk>\d+)/profile/update/$',views.profile_update,name='profile_update'),#更新个人信息
    re_path(r'user/(?P<pk>\d+)/pwd_change/$',views.pwd_change,name='pwd_change'),#修改密码
    re_path(r'logout/$',views.LogoutView,name='logout'),#退出登录
    re_path(r'index/',views.index,name="index"),
    re_path(r'account/',viewsmaterial.account,name="account"),
    re_path(r'data/',viewsmaterial.data,name="data"),
    re_path(r'tool/',viewstools.bsjtool,name="bsjtool"),
    # re_path(r'datacheck/',viewstools.check_bsj_data,name="check"),
    re_path(r'tbl_setting/',views.tbl_setting,name="tbl_setting"),
    re_path(r'report/',viewsreport.report,name="report"),

]