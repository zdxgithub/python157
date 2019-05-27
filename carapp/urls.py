from django.urls import path
from carapp.views import carlist,carlistlogic,addcar,upcar,car_remove,car_recover

# app_name = 'carapp'
app_name = 'carapp'

urlpatterns = [
    path('carlist/',carlist, name='carlist'),
    path('carlistlogic/',carlistlogic,name='carlistlogic'),
    path('addcar/', addcar, name='addcar'),
    path('upcar/', upcar, name='upcar'),
    path('car_recover/',car_recover,name='car_recover'),
    path('car_remove/', car_remove, name='car_remove'),
]