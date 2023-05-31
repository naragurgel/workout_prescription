from django import forms
from .models import Exercise, Workout, WorkoutItem


class ExerciseForm(forms.ModelForm):
    """
    A form for creating and updating Exercise objects.

    Inherits from Django's ModelForm class and is linked to the Exercise model.

    Fields:
    - name: CharField representing the name of the exercise.

    Meta:
    - model: Exercise model class to associate the form with.
    - fields: List of fields to include in the form.

    Usage Example:
    form = ExerciseForm()
    """
    class Meta:
        model = Exercise
        fields = ['name']


class WorkoutItemForm(forms.ModelForm):
    """
    A form for creating and updating WorkoutItem objects.

    Inherits from Django's ModelForm class and is linked to the WorkoutItem model.

    Fields:
    - sets: PositiveIntegerField representing the number of sets for the workout item.
    - reps: PositiveIntegerField representing the number of reps for the workout item.
    - exercise: ForeignKey field representing the exercise associated with the workout item.

    Meta:
    - model: WorkoutItem model class to associate the form with.
    - fields: List of fields to include in the form.

    Usage Example:
    form = WorkoutItemForm()
    """
    class Meta:
        model = WorkoutItem
        fields = ['sets', 'reps', 'exercise']


class WorkoutForm(forms.ModelForm):
    """
    A form for creating and updating Workout objects.

    Inherits from Django's ModelForm class and is linked to the Workout model.

    Fields:
    - owner: ForeignKey field representing the owner (user) of the workout.
    - name: CharField representing the name of the workout.
    - instructions: TextField representing the instructions for the workout.
    - exercises: ManyToManyField representing the exercises associated with the workout.

    Meta:
    - model: Workout model class to associate the form with.
    - fields: List of fields to include in the form.

    Usage Example:
    form = WorkoutForm()
    """
    class Meta:
        model = Workout
        fields = ['owner', 'name', 'instructions', 'exercises']
