from django.db import models

# Create your models here.

class ReadingMaterial(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=400, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-pk']
