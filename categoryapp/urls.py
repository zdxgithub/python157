from django.urls import path
from categoryapp.views import booklist

app_name = 'categoryapp'
urlpatterns = [
    path('booklist/',booklist,name='booklist'),
]