from django.conf.urls import url
from projects import views

urlpatterns = [
		url(r'^$', views.projects_home, name='projects')
]