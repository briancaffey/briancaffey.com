from django.db import models
from django.conf import settings
# Create your models here.
from comments.models import Comment #users can comment on reading list

from taggit.managers import TaggableManager

from django.contrib.auth.models import User



class ReadingMaterial(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=400, unique=True)
    tags = TaggableManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-pk']
