from django.db import models
from django.utils.translation import gettext_lazy as _


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
        return f"{self.exercise}: sets - {self.sets} reps - {self.sets}"


class WorkoutSheet(models.Model):
    name = models.CharField(max_length=100)