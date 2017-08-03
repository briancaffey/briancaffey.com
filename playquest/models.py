from django.db import models
from hashid_field import HashidAutoField
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.postgres.fields import JSONField

class Game(models.Model):
    id = HashidAutoField(primary_key=True)
    game_data = JSONField()
    game_owner = models.ForeignKey(User, blank=True, null=True)
    game_name = models.CharField(max_length=200)
    game_emoji = models.CharField(max_length=200)
    game_created = models.DateTimeField(auto_now_add=True)
    game_updated = models.DateTimeField(auto_now=True)
    game_saved = models.BooleanField(default=False)
    game_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-game_created']

    def __str__(self):
        return str(self.id)

    def play_url(self):
        return reverse('playquest:game_id', args=[self.id])

class GamePlay(models.Model):
    game_id = models.ForeignKey(Game, blank=True, null=True)
    player = models.ForeignKey(User, blank=True, null=True)
    gameplay_uid = models.CharField(default=uuid.uuid4, max_length=40)
    game_created = models.DateTimeField(auto_now_add=True)
    game_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(game_id) + " -- " + str(game_created)
