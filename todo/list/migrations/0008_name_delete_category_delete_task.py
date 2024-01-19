# Generated by Django 4.2.2 on 2023-10-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0007_remove_task_priority_remove_task_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=25)),
                ('second', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]