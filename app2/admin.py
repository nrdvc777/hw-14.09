from django.contrib import admin

# Register your models here.
from .models import ToDoModel
admin.site.register(ToDoModel)