from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Workout, WorkoutItem, Exercise
# Register your models here.


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    """
    Admin class for Exercise model.
    """
    search_fields = ['name']


@admin.register(WorkoutItem)
class WorkoutItemAdmin(admin.ModelAdmin):
    """
    Admin class for WorkoutItem model.
    """
    search_fields = ['exercise']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    """
    Admin class for Workout model.
    """
    list_display = ['owner', 'name']
    search_fields = ['name', 'owner']

    ordering = ['owner']
