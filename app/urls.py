from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='index'),
    path('login', views.login, name='index'),
    path('back', views.back, name='index'),
    
    
]
