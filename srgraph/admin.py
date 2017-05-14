from django.contrib import admin
from .models import Subreddit, SearchResult
# Register your models here.

admin.site.register(Subreddit)

admin.site.register(SearchResult)
