from django.db import models
from hashid_field import HashidAutoField
from django.contrib.auth.models import User
import uuid
# Create your models here.

class HashItem(models.Model):
    id = HashidAutoField(primary_key=True)
    item_owner = models.ForeignKey(User, blank=True, null=True)


    def __str__(self):
        return str(self.id)


class HashItemReferencingItem(models.Model):
    item = models.ForeignKey(HashItem, blank=True, null=True)
    item_uid = models.CharField(default=uuid.uuid4, max_length=40)

    def __str__(self):
        return str(self.item) + str(self.item_uid)
