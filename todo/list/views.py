from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .Serializer import *
from .models import *


# Create your views here.
@api_view(['GET'])
def index (request):
    api_url={
        'list': '/task-list/',
        'disc': '/task-disc/<str:pk>/',
        'create': '/task-create/<str:pk>/',
        'delete': '/task-delete/<str:pk>/',
        'update': '/task-update/<str:pk>/',

    }
    return Response(api_url)
@api_view(['GET'])
def TaskList(request):
    tasks =Task.objects.all()
    serializer =TaskSerializer(tasks, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def TaskDetal(request,pk):
    tasks =Task.objects.get(id=pk)
    serializer =TaskSerializer(tasks, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def TaskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return (Response(serializer.data)

@api_view(['POST']))
def CategoryCreate(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def TaskUpdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def TaskDelete(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return (Response("done")
@api_view(['DELETE']))
def CategoryDelete(request,pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("done")

# PUT
# PATCH

