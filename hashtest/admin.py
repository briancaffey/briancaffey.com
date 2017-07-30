from django.contrib import admin
from .models import HashItem, HashItemReferencingItem
# Register your models here.

admin.site.register(HashItem)

admin.site.register(HashItemReferencingItem)
