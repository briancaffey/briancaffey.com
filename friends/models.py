from django.db import models
from accounts.models import UserProfile

# Create your models here.


class Friend(models.Model):
    users = models.ManyToManyField(UserProfile)
    current_user = models.ForeignKey(UserProfile, related_name="owner", null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user = current_user
        )
        friend.users.remove(new_friend)
