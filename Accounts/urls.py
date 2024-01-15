
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
     path('', views.Home,name='login'),
     path('signup',views.Signup,name='signup'),
     path('login',views.Login,name='signin')
]
