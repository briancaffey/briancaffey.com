from django.conf.urls import url, include
from django.conf import settings
from .views import (

	comment_thread,

	)

urlpatterns = [
	
	url(r'^(?P<pk>\d+)/$', comment_thread, name="thread"),

]
