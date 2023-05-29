from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class WorkoutItem(models.Model):
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
    )
    reps = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exercise}: sets - {self.sets} reps - {self.reps}"


class Workout(models.Model):
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
