from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Game(models.Model):
    game = JSONField()

    def __str__(self):
        return str(self.id)
