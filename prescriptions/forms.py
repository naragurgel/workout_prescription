from django import forms
from .models import Workout, WorkoutSheet, WorkoutPrescription


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description']  


class WorkoutSheetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSheet
        fields = ['name']


class WorkoutPrescriptionForm(forms.ModelForm):
    class Meta:
        model = WorkoutPrescription
        fields = ['set', 'rep', 'workout', 'workout_sheet', 'day_of_week']