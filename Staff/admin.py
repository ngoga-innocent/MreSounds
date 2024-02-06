from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Skills)
admin.site.register(models.Chapter)
admin.site.register(models.Team)