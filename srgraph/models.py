import ast
from django.db import models
from datetime import datetime, timedelta
from django.utils.timezone import now


# Create your models here.

class Subreddit(models.Model):
    name = models.CharField(max_length=400, blank=True, null=True)

    def __str__(self):
        return str(self.name)

    def reddit_link(self):
        return "https://reddit.com" + self.name.strip('\n')


class SearchResult(models.Model):
    s_one = models.ForeignKey(Subreddit, related_name='s1')
    s_two = models.ForeignKey(Subreddit, related_name='s2')
    path = models.CharField(max_length=1000)
    votes = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    last_searched = models.DateTimeField(default=now, blank=True)

    class Meta:
        ordering = ['-last_searched']

    def __str__(self):
        return str(self.s_one.name + " - "+ self.s_two.name)

    def api_like_link(self):
        return '/api/result-up/' + str(self.id)

    def api_dislike_link(self):
        return '/api/result-down/' + str(self.id)

    def get_list(self):
        path = self.path
        path = ast.literal_eval(path)
        print(path)
        # path = list(set(path))
        print(path)
        unique_collection = []
        for x in path:
            sr = Subreddit.objects.filter(name=x).first()
            dic = {'sr':sr}
            if sr not in unique_collection:
                unique_collection.append(dic)

        return unique_collection








#
