
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
     path('', views.Home,name='home'),
     path('allcourse',views.AllCourse,name='all_courses'),
     path('course/<str:id>',views.Singlecourse,name='single_course'),
     path('payment/<str:id>',views.PaymentFunction,name="payment")
]
