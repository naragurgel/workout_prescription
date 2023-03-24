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


class Workout_prescription(models.Model):
    set = models.IntegerField()
    rep = models.IntegerField()
    workout = models.ForeignKey(Workout, models.CASCADE)


class Workout_sheet(models.Model):
    name = models.CharField(max_length=100)
    mon = models.ManyToManyField(Workout, null=True, blank=True, related_name='mon')
    tue = models.ManyToManyField(Workout, null=True, blank=True, related_name='tue')
    wed = models.ManyToManyField(Workout, null=True, blank=True, related_name='wed')
    thu = models.ManyToManyField(Workout, null=True, blank=True, related_name='thu')
    fri = models.ManyToManyField(Workout, null=True, blank=True, related_name='fri')
    sat = models.ManyToManyField(Workout, null=True, blank=True, related_name='sat')
    sun = models.ManyToManyField(Workout, null=True, blank=True, related_name='sun')