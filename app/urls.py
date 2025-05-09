from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='index'),
    # path('login', views.login, name='index'),
    
    
]
