from django.conf.urls import url, include
from .views import projects_home

urlpatterns = [
		url(r'^$', projects_home, name='projects'),

]
