from django.urls import path
from .views import workout, workout_sheet

urlpatterns = [
    path('workout', workout.list, name='workout_list'),
    path('workout/create/', workout.create, name='workout_create'),
    path('workout/update/<int:pk>/', workout.update, name='workout_update'),
    path('workout/delete/<int:pk>/', workout.delete, name='workout_delete'),
    path('workout_sheet', workout_sheet.list, name='workout_sheet_list'),
    path('workout_sheet/create/', workout_sheet.create, name='workout_sheet_create'),
    path('workout_sheet/update/<int:pk>/', workout_sheet.update, name='workout_sheet_update'),
    path('workout_sheet/delete/<int:pk>/', workout_sheet.delete, name='workout_sheet_delete'),

]
