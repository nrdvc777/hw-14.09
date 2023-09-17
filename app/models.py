from django.db import models
from datetime import datetime
# Create your models here.
from django.contrib.auth.models import User

class ToDoModel(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=77, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'Todos'