from django import forms
from .models import MuscleGroup, Equipment, Workout


class MuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'difficulty', 'duration', 'muscle_groups', 'equipment']  # noqa
