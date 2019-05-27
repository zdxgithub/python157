from django.urls import path
from lrapp.views import login, regist, registlogic, checkname, checkpwd, checkrepwd, getcaptcha, code, loginlogic, \
    registjump, checklpwd, checklname, email_check, email_check_ok, emaillogic

app_name = 'lrapp'
urlpatterns = [
    path('login/',login,name='login'),
    path('regist/', regist, name='regist'),
    path('registlogic/', registlogic, name='registlogic'),
    path('checkname/',checkname,name='checkname'),
    path('checkpwd/',checkpwd,name='checkpwd'),
    path('checkrepwd/',checkrepwd,name='checkrepwd'),
    path('getcaptcha/',getcaptcha,name='getcaptcha'),
    path('code/',code,name='code'),
    path('loginlogic/',loginlogic,name='loginlogic'),
    path('registjump/',registjump,name='registjump'),
    path('checklpwd',checklpwd,name='checklpwd'),
    path('checklname', checklname, name='checklname'),
    path('email_check', email_check, name='email_check'),
    path('email_check_ok', email_check_ok, name='email_check_ok'),
    path('emaillogic', emaillogic, name='emaillogic'),
]