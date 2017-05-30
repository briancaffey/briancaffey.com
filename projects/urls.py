from django.conf.urls import url, include
from projects import views

urlpatterns = [
		url(r'^$', views.projects_home, name='projects'),
		url(r'^bokeh/$', views.bokeh, name='bokeh'),
		url(r'^kingsencounter/$', views.kings, name='kings'),

]
