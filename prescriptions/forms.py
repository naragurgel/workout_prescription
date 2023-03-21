from django import forms
from .models import MuscleGroup, Equipment


class MuscleGroupForm(forms.ModelForm):
    class Meta:
        model = MuscleGroup
        fields = ['name']


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name']
