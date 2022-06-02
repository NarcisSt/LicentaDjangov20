from django.db import models


class Teams(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()
    city = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)
