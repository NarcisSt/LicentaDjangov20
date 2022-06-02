from django.db import models


class PlayerData(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    shirt_number = models.BigIntegerField()
    position = models.TextField()
    age = models.BigIntegerField()
    team = models.ForeignKey('Teams', models.DO_NOTHING, db_column='team')
