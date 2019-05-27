from django.urls import path
from homeapp.views import home,h_login,h_regist,h_bookdetails

app_name = 'homeapp'
urlpatterns = [
    path('home/',home,name='home'),
    path('h_login/',h_login,name='h_login'),
    path('h_regist',h_regist,name='h_regist'),
    path('h_bookdetails/', h_bookdetails, name='h_bookdetails'),
]