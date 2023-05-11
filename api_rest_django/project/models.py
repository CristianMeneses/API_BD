from django.db import models
from django.utils import timezone

# Create your models here.
class project(models.Model):
    
    project_id = models.IntegerField(max_length=10)
    description = models.TextField(default='DEFAULT VALUE')
    name = models.CharField(max_length=50, default='DEFAULT VALUE')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=50, default='DEFAULT VALUE')     
        
    class Meta:
        db_table = 'project'