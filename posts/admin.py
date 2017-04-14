from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ['__str__', 'updated', 'timestamp']
	list_display_links = ['updated']
	list_filter = ['updated']
	search_fields = ['title', 'content']
	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
