from django.urls import path
from .views import muscle_group

urlpatterns = [
    path('home', muscle_group.list, name='home'), ## todo create a real home page
    path('', muscle_group.list, name='muscle_group_list'),
    path('create/', muscle_group.create, name='muscle_group_create'),
    path('update/<int:pk>/', muscle_group.update, name='muscle_group_update'),
    path('delete/<int:pk>/', muscle_group.delete, name='muscle_group_delete'),
]
