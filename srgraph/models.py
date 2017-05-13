from django.db import models

# Create your models here.

class Subreddit(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def reddit_link(self):
        return "https://reddit.com" + self.name.strip('\n')
