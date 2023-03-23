from django.urls import path
from .views import muscle_group, equipment, workout

urlpatterns = [
    path('home', muscle_group.list, name='home'), ## todo create a real home page
    path('muscle_group', muscle_group.list, name='muscle_group_list'),
    path('muscle_group/create/', muscle_group.create, name='muscle_group_create'),
    path('muscle_group/update/<int:pk>/', muscle_group.update, name='muscle_group_update'),
    path('muscle_group/delete/<int:pk>/', muscle_group.delete, name='muscle_group_delete'),
    path('equipment', equipment.list, name='equipment_list'),
    path('equipment/create/', equipment.create, name='equipment_create'),
    path('equipment/update/<int:pk>/', equipment.update, name='equipment_update'),
    path('equipment/delete/<int:pk>/', equipment.delete, name='equipment_delete'),
    path('workout', workout.list, name='workout_list'),
    path('workout/create/', workout.create, name='workout_create'),
    path('workout/update/<int:pk>/', workout.update, name='workout_update'),
    path('workout/delete/<int:pk>/', workout.delete, name='workout_delete'),
]
