from django.contrib import admin

# Register your models here.

admin.site.site_header = "曜立 | Yawlih"

from .models import Company, Job, News, Investor, Investment
# Register your models here.

admin.site.register(Company)

admin.site.register(Job)

admin.site.register(News)


admin.site.register(Investor)

admin.site.register(Investment)
