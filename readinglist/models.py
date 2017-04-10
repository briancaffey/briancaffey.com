from django.db import models
from django.conf import settings
# Create your models here.

class ReadingMaterial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=400, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-pk']
