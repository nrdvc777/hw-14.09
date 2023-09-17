from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class TodoModel(models.Model):
    task_name = models.CharField(max_length=25, default='')
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    status = models.BooleanField(default=False)
    description = models.CharField(max_length=25, default='')
    user = models.ForeignKey(User)

    def __str__(self) -> str:
        return self.task_name
    
    # class Meta:
    #     db_table = 'Todos'