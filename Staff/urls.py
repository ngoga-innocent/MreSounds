
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
     path('', views.Home),
     path('addcourse',views.AddCourse, name='addcourse'),
     path('addcourse/<str:id>',views.ViewChapter,name="view_chapter"),
     path('addcourse/<str:course_id>/<str:chapter_id>/',views.AddSkill, name='addcourse'),
     path('getskills/<str:id>/',views.GetSkills,name='get_skills'),
     path('skill/<str:id>',views.SingleSkill,name='skill'),
     path('addchapter/<str:id>',views.AddChapter,name='addchapter')
     
]
