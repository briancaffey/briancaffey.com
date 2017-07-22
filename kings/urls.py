from django.conf.urls import url, include
from kings import views

urlpatterns = [
		url(r'^kingsencounter/level_builder/$', views.level_builder, name='level_builder'),
		url(r'^kingsencounter/v2/$', views.kings_two, name='kings2'),
		url(r'^kingsencounter/v3/$', views.kings_three, name='kings3'),
		url(r'^kingsencounter/$', views.kings_two, name='kings'),

]
