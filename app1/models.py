from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import datetime
from django.db.models import *
class TodoModel(Model):
    name = CharField(max_length=50)
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)
    description = CharField(max_length=77, default='')
    user = ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return self.name
