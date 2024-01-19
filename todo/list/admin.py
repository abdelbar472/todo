from django.contrib import admin
from .models import *
from .Serializer import *
# Register your models here.
admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Name)
