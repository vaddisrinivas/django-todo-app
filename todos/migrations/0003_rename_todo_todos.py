# Generated by Django 4.1.7 on 2023-04-03 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_todo_delete_task_delete_taskspecial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Todo", new_name="Todos",),
    ]