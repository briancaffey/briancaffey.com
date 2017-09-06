from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100, default='')
	twitter = models.CharField(max_length=100, default='')
	emoji = models.CharField(max_length=10, default='')

	def __str__(self):
		return self.user.username

	def get_absolute_url(self):
		return "/users/%i/" % self.id

	def friend_toggle(self):
		pass

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
