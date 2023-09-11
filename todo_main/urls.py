from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('addtask/',views.AddTask, name='AddTask'),
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/',views.mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:pk>/',views.edit_task, name='edit_task'),
    path('delete/<int:pk>/',views.delete, name='delete'),
]