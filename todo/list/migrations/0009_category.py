# Generated by Django 4.2.2 on 2023-10-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0008_name_delete_category_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
            ],
        ),
    ]