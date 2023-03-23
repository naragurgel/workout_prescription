from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.IntegerField()
    duration = models.DurationField()
    muscle_groups = models.ManyToManyField(MuscleGroup)
    equipment = models.ManyToManyField(Equipment)

    def __str__(self):
        return self.name
