from django.conf.urls import url, include
from projects import views

urlpatterns = [
		url(r'^$', views.projects_home, name='projects'),
		url(r'^bokeh/$', views.bokeh, name='bokeh'),
		url(r'^kingsencounter/v2/$', views.kings_two, name='kings2'),
		url(r'^kingsencounter/$', views.kings_two, name='kings'),

]
