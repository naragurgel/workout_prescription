from django.db import models
from django.utils.translation import gettext_lazy as _


class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class WorkoutSheet(models.Model):
    name = models.CharField(max_length=100)


class WorkoutPrescription(models.Model):
    class DayOfWeek(models.TextChoices):
        MONDAY = 'MO', _('Monday')
        TUESDAY = 'TU', _('Tuesday')
        WEDNESDAY = 'WE', _('Wednesday')
        THURDAY = 'TH', _('Thurday')
        FRIDAY = 'FR', _('Friday')
        SATURDAY = 'SA', _('Saturday')
        SUNDAY = 'SU', _('Sunday')
    day_of_week = models.CharField(
        max_length=2,
        choices=DayOfWeek.choices,
    )
    set = models.IntegerField()
    rep = models.IntegerField()
    workout = models.ForeignKey(Workout, models.CASCADE)
    workout_sheet = models.ForeignKey(WorkoutSheet, models.CASCADE)