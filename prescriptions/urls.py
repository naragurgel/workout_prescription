from django.urls import path
from .views import exercise, workout_sheet, workout_prescription

urlpatterns = [
    path('exercise', exercise.list, name='exercise_list'),
    path('exercise/create/', exercise.create, name='exercise_create'),
    path('exercise/update/<int:pk>/', exercise.update, name='exercise_update'),
    path('exercise/delete/<int:pk>/', exercise.delete, name='exercise_delete'),
    path('workout_sheet', workout_sheet.list, name='workout_sheet_list'),
    path('workout_sheet/create/', workout_sheet.create, name='workout_sheet_create'),
    path('workout_sheet/update/<int:pk>/', workout_sheet.update, name='workout_sheet_update'),
    path('workout_sheet/details/<int:pk>/', workout_sheet.details, name='workout_sheet_details'),
    path('workout_sheet/delete/<int:pk>/', workout_sheet.delete, name='workout_sheet_delete'),
    path('workout_prescription/create/<int:workout_sheet_id>/<str:day_of_week>/', workout_prescription.create, name='workout_prescription_create'),
    path('workout_prescription/update/<int:pk>/<int:workout_sheet_id>/', workout_prescription.update, name='workout_prescription_update'),
    path('workout_prescription/delete/<int:pk>/<int:workout_sheet_id>/', workout_prescription.delete, name='workout_prescription_delete'),

]
