from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    task_name = models.CharField(max_length=30)
    task_category = [
        ('work','Work'),
        ('personal','Personal'),
        ('study','Study'),
        ('shoping','Shoping'),
        ('health','Health'),
        ('fitness','Fitness'),
        ('travel','Travel'),
        ('other','other'),
    ]
    category = models.CharField(max_length=15,choices=task_category)
    assigned_date = models.DateField(auto_now=True)
    priority_category = [
        ('low','Low'),
        ('medium','Medium'),
        ('high','High'),
    ]
    priority = models.CharField(max_length=10,choices=priority_category)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.task_name} has been created and is currently in progress {self.priority}"
    