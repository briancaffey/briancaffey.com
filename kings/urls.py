from django.conf.urls import url, include
from kings import views
from kings.api.views import GameCreateAPIView, GameListAPIView, GameDetailAPIView, GameUpdateAPIView
urlpatterns = [
		url(r'^start/$', views.level_builder, name='level_builder'),
		url(r'^kingsencounter/v2/$', views.kings_two, name='pilot'),
		url(r'^kingsencounter/v3/$', views.kings_three, name='kings3'),
		url(r'^new/$', views.kings_four, name='demo'),
		url(r'^kingsencounter/(?P<id>\d+)$', views.game_id, name='kings4'),
		url(r'^kingsencounter/$', views.kings_two, name='kings'),
		url(r'^kingsencounter/json/$', views.sample_json, name="sample_json"),

		# API CRU[D] endpoints coming from /api/kings/ (in main urls.py)
		url(r'^(?P<pk>\d+)/update/$', GameUpdateAPIView.as_view(), name="update-game"),
		url(r'^(?P<pk>\d+)/$', GameDetailAPIView.as_view(), name="save-game"),
		url(r'^save/$', GameCreateAPIView.as_view(), name="save-game"),
		# url(r'^games/$', GameListAPIView.as_view(), name="list-game"),

]
