# Generated by Django 4.1.2 on 2022-10-10 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_datecompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='memo',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
