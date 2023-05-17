from django import forms
from .models import Exercise, Workout, WorkoutItem


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']  


class WorkoutSheetForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name']


class WorkoutItemForm(forms.ModelForm):
    class Meta:
        model = WorkoutItem
        fields = ['sets', 'reps', 'exercise']

