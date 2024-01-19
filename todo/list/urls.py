from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='todo_index'),
    path('list/', views.TaskList, name='todo_TaskList'),
    path('detal/<str:pk>/', views.TaskDetal, name='todo_TaskDetal'),
    path('update/<str:pk>/', views.TaskUpdate, name='todo_TaskUpdate '),
    path('delete/<str:pk>/', views.TaskDelete, name='todo_TaskDelete '),
    path('delete/category/<str:pk>/', views.CategoryDelete, name='todo_CategoryDelete '),
    path('create/', views.TaskCreate, name='todo_Create'),
    path('create/category/', views.CategoryCreate, name='todo_CategoryCreate'),

]
