from django.urls import path
from . import views

urlpatterns = [
    path('home', views.muscle_group_list, name='home'), ## todo create a real home page
    path('', views.muscle_group_list, name='muscle_group_list'),
    path('create/', views.muscle_group_create, name='muscle_group_create'),
    path('update/<int:pk>/', views.muscle_group_update, name='muscle_group_update'),
    path('delete/<int:pk>/', views.muscle_group_delete, name='muscle_group_delete'),
]
