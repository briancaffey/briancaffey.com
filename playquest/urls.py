from django.conf.urls import url, include
from playquest import views
from playquest.api.views import GameCreateAPIView, GameListAPIView, GameDetailAPIView, GameUpdateAPIView
urlpatterns = [
		url(r'^create/$', views.create, name='create'),
		url(r'^demo/$', views.demo, name='demo'),
		url(r'^$', views.playquest_home, name="home"),
		url(r'^game/(?P<id>[A-Za-z0-9]+)/$', views.game_id, name='game_id'),
		url(r'^json/$', views.sample_json, name="sample_json"),
		## To Do
		url(r'^game/(?P<id>[A-Za-z0-9]+)/edit/$', views.edit_game, name="edit"),

		# API CRU[D] endpoints coming from /api/kings/ (in main urls.py)
		url(r'^(?P<pk>[A-Za-z0-9]+)/update/$', GameUpdateAPIView.as_view(), name="update-game"),
		url(r'^(?P<pk>[A-Za-z0-9]+)/$', GameDetailAPIView.as_view(), name="save-game"),
		url(r'^save/$', GameCreateAPIView.as_view(), name="save-game"),

]
