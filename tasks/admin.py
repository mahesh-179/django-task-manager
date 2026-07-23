from django.contrib import admin
from .models import Task,Profile
# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display = ['user','task_name','category','assigned_date','priority']

admin.site.register(Task,AdminTask)

class AdminProfile(admin.ModelAdmin):
    list_display = ["user","full_name","address","phno"]

admin.site.register(Profile,AdminProfile)