from django.db import models


# Create your models here.
class Players(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    shirt_number = models.BigIntegerField()
    position = models.TextField()
    age = models.BigIntegerField()
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team')

    class Meta:
        managed = False
        db_table = 'players'


class Teams(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()
    city = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'
