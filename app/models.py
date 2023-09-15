from django.db import models

# Create your models here.
from datetime import datetime
from django.db.models import *
class TodoModel(Model):
    name = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    description = CharField(max_length=77, default='')

    def __str__(self) -> str:
        return self.name
    
    # class Meta:
    #     db_table = "Todos"