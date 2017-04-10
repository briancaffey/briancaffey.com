from django.db import models

# Create your models here.

class NewsletterEmails(models.Model):
    email = models.EmailField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.email)
