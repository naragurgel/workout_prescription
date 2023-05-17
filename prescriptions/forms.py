from django import forms
from .models import Exercise, WorkoutSheet, WorkoutPrescription


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name']  


class WorkoutSheetForm(forms.ModelForm):
    class Meta:
        model = WorkoutSheet
        fields = ['name']


class WorkoutPrescriptionForm(forms.ModelForm):
    class Meta:
        model = WorkoutPrescription
        fields = ['set', 'rep', 'workout', 'workout_sheet', 'day_of_week']
        widgets = {
            'day_of_week': forms.HiddenInput(),
            'workout_sheet': forms.HiddenInput()
        }