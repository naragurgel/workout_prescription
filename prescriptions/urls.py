from django.urls import path
from .views import exercise, workout_sheet, workout_item

urlpatterns = [
    path('exercise', exercise.list, name='exercise_list'),
    path('exercise/create/', exercise.create, name='exercise_create'),
    path('exercise/update/<int:pk>/', exercise.update, name='exercise_update'),
    path('exercise/delete/<int:pk>/', exercise.delete, name='exercise_delete'),
    path('workout_sheet', workout_sheet.list, name='workout_sheet_list'),
    path('workout_sheet/create/', workout_sheet.create, name='workout_sheet_create'),
    path('workout_sheet/update/<int:pk>/', workout_sheet.update, name='workout_sheet_update'),
    # path('workout_sheet/details/<int:pk>/', workout_sheet.details, name='workout_sheet_details'),
    path('workout_sheet/delete/<int:pk>/', workout_sheet.delete, name='workout_sheet_delete'),
    path('workout_item/create/', workout_item.create, name='workout_item_create'),
    path('workout_item/update/<int:pk>/', workout_item.update, name='workout_item_update'),
    path('workout_item/delete/<int:pk>/', workout_item.delete, name='workout_item_delete'),

]
