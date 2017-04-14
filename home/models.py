from django.db import models
from django.conf import settings
# Create your models here.

class NewsletterEmails(models.Model):
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)


class GuestBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    message = models.CharField(max_length=400)
    date_created = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user + '--' + self.message)
