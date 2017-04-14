from django.contrib import admin

# Register your models here.
from .models import NewsletterEmails, GuestBook

class NewsletterEmailsModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'confirmed', 'uid']
    list_filter = ['confirmed']
    class Meta:
        model = NewsletterEmails





admin.site.register(NewsletterEmails, NewsletterEmailsModelAdmin)
