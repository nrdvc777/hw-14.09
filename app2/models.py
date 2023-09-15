from django.db import models
from django.db.models import *
# Create your models here.
from datetime import datetime

class ToDoModel(Model):
    name = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    status = BooleanField(default=False)
    description = CharField(max_length=70)

    def __str__(self) -> str:
        return self.name
