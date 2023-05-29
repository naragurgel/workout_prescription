from django import forms
from .models import Exercise, Workout, WorkoutItem


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']


class WorkoutItemForm(forms.ModelForm):
    class Meta:
        model = WorkoutItem
        fields = ['sets', 'reps', 'exercise']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['owner', 'name', 'instructions', 'exercises']
