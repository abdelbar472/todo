# Generated by Django 4.2.2 on 2023-10-10 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('Priority', models.CharField(blank=True, choices=[('red', 'red'), ('yellow', 'yellow'), ('blue', 'blue'), ('white', 'white')], max_length=25, null=True)),
                ('catagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='list.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
