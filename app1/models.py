from django.db import models
from datetime import datetime
# Create your models here.

class TodoModel(models.Model):
    task_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.CharField(default='', max_length=77)

    def __str__(self) -> str:
        return self.task_name
    
    class Meta:
        db_table = 'Todos'