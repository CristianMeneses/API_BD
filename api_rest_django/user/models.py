from django.db import models
from django.utils import timezone

# Create your models here.
class user(models.Model):

    user_id = models.IntegerField(max_length=10)
    username = models.CharField(max_length=50, default='DEFAULT VALUE')
    password = models.CharField(max_length=200, default='DEFAULT VALUE')
    profesional_headline = models.CharField(max_length=50, default='DEFAULT VALUE')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_id = models.IntegerField(max_length=10)
        
    class Meta:
        db_table = 'user'