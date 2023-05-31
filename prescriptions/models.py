from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
     """
    Model representing an exercise.

    Fields:
    - name: CharField representing the name of the exercise.

    Methods:
    - __str__: Returns a string representation of the exercise object.

    Usage Example:
    exercise = Exercise.objects.get(id=1)
    print(exercise)
    """
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class WorkoutItem(models.Model):
    """
    Model representing a workout item.

    Fields:
    - exercise: ForeignKey field representing the exercise associated with the workout item.
    - reps: PositiveIntegerField representing the number of repetitions for the workout item.
    - sets: PositiveIntegerField representing the number of sets for the workout item.

    Methods:
    - __str__: Returns a string representation of the workout item object.

    Usage Example:
    workout_item = WorkoutItem.objects.get(id=1)
    print(workout_item)
    """
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
    )
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise}: sets - {self.sets} reps - {self.reps}"


class Workout(models.Model):
    """
    Model representing a workout.

    Fields:
    - owner: ForeignKey field representing the owner (user) of the workout.
    - name: CharField representing the name of the workout.
    - instructions: TextField representing the instructions for the workout.
    - exercises: ManyToManyField representing the exercises associated with the workout.

    Methods:
    - __str__: Returns a string representation of the workout object.

    Usage Example:
    workout = Workout.objects.get(id=1)
    print(workout)
    """
    owner = models.ForeignKey(
        User,
        related_name="user_id",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=250, unique=True)
    instructions = models.TextField(max_length=1000, null=True, blank=True)
    exercises = models.ManyToManyField(
        WorkoutItem
    )

    def __str__(self):
        return f"{self.owner}: {self.name}"
