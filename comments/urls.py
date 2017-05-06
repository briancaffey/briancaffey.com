from django.conf.urls import url, include
from django.conf import settings
from .views import (

	comment_thread,
	comment_delete,

	)

urlpatterns = [

	url(r'^(?P<pk>\d+)/$', comment_thread, name="thread"),
	url(r'^(?P<pk>\d+)/delete/$', comment_delete, name="delete"),
	

]
