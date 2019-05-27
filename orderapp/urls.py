from django.conf.urls import url
from django.contrib import admin
from orderapp.views import order_indent,checkname,checkadress,checkcode,checkphone,order_indentlogic,page1,page2,index,indentok,checkad
from django.urls import path


app_name = 'orderapp'
urlpatterns = [
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^page1/', page1,name='page1'),
    url(r'^page2/', page2,name='page2'),
    path('index/', index,name='index'),
    path('order_indent/',order_indent,name='order_indent'),
    path('checkname/',checkname,name='checkname'),
    path('checkadress/', checkadress, name='checkadress'),
    path('checkcode/', checkcode, name='checkcode'),
    path('checkphone/', checkphone, name='checkphone'),
    path('order_indentlogic/', order_indentlogic, name='order_indentlogic'),
    path('indentok/', indentok, name='indentok'),
    path('checkad/', checkad, name='checkad'),
]