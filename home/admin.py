from django.contrib import admin

# Register your models here.
from .models import NewsletterEmails, GuestBook

admin.site.register(NewsletterEmails)

admin.site.register(GuestBook)
