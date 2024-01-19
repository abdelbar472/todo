from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=12)
    def __str__(self):
        return self.name

class Task(models.Model):
    Priority_task= [
        ('red', 'red'),
        ('yellow', 'yellow'),
        ('blue', 'blue'),
        ('white', 'white'),

    ]
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=250, null=True, blank=True)
    media = models.FileField(upload_to='media', null=True, blank=True)
    active = models.BooleanField(default=False)
    Priority = models.CharField(max_length=25, choices=Priority_task, null=True, blank=True)
    catagory = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

class Name(models.Model):
    first = models.CharField(max_length=25)
    second = models.CharField(max_length=25)
    def __str__(self):
        return self.first