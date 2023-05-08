from django import forms
from .models import Workout, WorkoutSheet


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']  


class WorkoutSheetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSheet
        fields = ['name', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']