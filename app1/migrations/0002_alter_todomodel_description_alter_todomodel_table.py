# Generated by Django 4.1.7 on 2023-09-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterModelTable(
            name='todomodel',
            table='Todos',
        ),
    ]
