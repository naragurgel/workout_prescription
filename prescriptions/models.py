from django.db import models


class MuscleGroup(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)

    def _str_(self):
        return self.name