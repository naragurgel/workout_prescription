from django.db import models


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class WorkoutPrescription(models.Model):
    set = models.IntegerField()
    rep = models.IntegerField()
    workout = models.ForeignKey(Workout, models.CASCADE)


class WorkoutSheet(models.Model):
    name = models.CharField(max_length=100)
    mon = models.ManyToManyField(Workout, blank=True, related_name='mon')
    tue = models.ManyToManyField(Workout, blank=True, related_name='tue')
    wed = models.ManyToManyField(Workout, blank=True, related_name='wed')
    thu = models.ManyToManyField(Workout, blank=True, related_name='thu')
    fri = models.ManyToManyField(Workout, blank=True, related_name='fri')
    sat = models.ManyToManyField(Workout, blank=True, related_name='sat')
    sun = models.ManyToManyField(Workout, blank=True, related_name='sun')
