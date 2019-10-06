from django.urls import path
from . import views

app_name = 'osr'

urlpatterns = [
    path('', views.sudokuform, name='form'),
    path('form/success/', views.success, name='success'),
]
