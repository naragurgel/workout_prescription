from django.urls import path
from .views import exercise, workout, workout_item

urlpatterns = [
    path('exercise', exercise.list, name='exercise_list'),
    path('exercise/create/', exercise.create, name='exercise_create'),
    path('exercise/update/<int:pk>/', exercise.update, name='exercise_update'),
    path('exercise/delete/<int:pk>/', exercise.delete, name='exercise_delete'),
    path('workout', workout.list, name='workout_list'),
    path('workout/create/', workout.create, name='workout_create'),
    path('workout/update/<int:pk>/', workout.update, name='workout_update'),
    path('workout/delete/<int:pk>/', workout.delete, name='workout_delete'),
    path('workout_item/', workout_item.list, name='workout_item_list'),
    path('workout_item/create/', workout_item.create, name='workout_item_create'),  # noqa
    path('workout_item/update/<int:pk>/', workout_item.update, name='workout_item_update'),  # noqa
    path('workout_item/delete/<int:pk>/', workout_item.delete, name='workout_item_delete'),  # noqa

]
