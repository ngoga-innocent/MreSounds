import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Course(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4,db_index=True)
    name=models.CharField(max_length=500)
    thumbnail=models.ImageField(upload_to='Course_Thumbnail')
    author=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    created_at=models.DateTimeField(default=timezone.now)
    paid_user=models.ManyToManyField(User,related_name='paid_course',blank=True)
    def __str__(self):
        return self.name
    
class Chapter(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    title=models.CharField(max_length=255)
    icon=models.ImageField(upload_to='Chapter_Icons',null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
class Skills(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    title=models.CharField(max_length=255)
    body=RichTextField(blank=True,null=True)
    exercise=RichTextField(blank=True,null=True)
    chapter=models.ForeignKey(Chapter,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Team(models.Model):
    id=models.UUIDField(primary_key=True,unique=True,editable=False,default=uuid.uuid4)
    name=models.CharField(max_length=255)
    position=models.CharField(max_length=255)
    thumbnail=models.ImageField(upload_to='Team_profile',null=True)

    def __str__(self):
        return self.name