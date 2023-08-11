from django.db import models


# Create your models here.
class TaskModel(models.Model):
    task_title = models.CharField(max_length=150)
    task_description= models.CharField(max_length=300)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task_title
    
