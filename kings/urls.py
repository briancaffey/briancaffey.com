from django.conf.urls import url, include
from kings import views
from kings.api.views import GameCreateAPIView, GameListAPIView, GameDetailAPIView, GameUpdateAPIView
urlpatterns = [
		url(r'^create/$', views.create, name='create'),
		url(r'^demo/$', views.demo, name='demo'),
		url(r'^$', views.kings_home, name="home"),
		url(r'^game/(?P<id>\d+)/$', views.game_id, name='game_id'),
		# url(r'^json/$', views.sample_json, name="sample_json"),
		## To Do
		# url(r'^game/(?P<id>\id+)/edit/$', views.edit_game, name="edit")

		# API CRU[D] endpoints coming from /api/kings/ (in main urls.py)
		url(r'^(?P<pk>\d+)/update/$', GameUpdateAPIView.as_view(), name="update-game"),
		url(r'^(?P<pk>\d+)/$', GameDetailAPIView.as_view(), name="save-game"),
		url(r'^save/$', GameCreateAPIView.as_view(), name="save-game"),
		# url(r'^games/$', GameListAPIView.as_view(), name="list-game"),
]
