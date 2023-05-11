from django.db import models
from django.utils import timezone

# Create your models here.
class enterprise(models.Model):
    
    enterprise_id = models.IntegerField(max_length=10)
    name = models.CharField(max_length=100, default='DEFAULT VALUE')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'enterprise'