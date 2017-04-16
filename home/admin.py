from django.contrib import admin

# Register your models here.
from .models import NewsletterEmails, GuestBook

class NewsletterEmailsModelAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'confirmed', 'uid']
    list_filter = ['confirmed']
    class Meta:
        model = NewsletterEmails


class GuestBookModelAdmin(admin.ModelAdmin):

    list_display = ['__str__',]
    list_filter = ['message']
    class Meta:
        model = GuestBook


admin.site.register(GuestBook, GuestBookModelAdmin)

admin.site.register(NewsletterEmails, NewsletterEmailsModelAdmin)
