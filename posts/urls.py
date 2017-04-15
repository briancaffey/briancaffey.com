from django.conf.urls import url
from posts.views import (
	posts_create,
	posts_list,
	posts_update,
	post_delete,
	posts_detail,
	posts_search,
	PostLikeToggle,
	PostLikeAPIToggle,
)


urlpatterns = [

	url(r'^api/(?P<slug>.+)/like/$', PostLikeAPIToggle.as_view(), name='like-api-toggle'),
	url(r'^(?P<slug>.+)/like/$', PostLikeToggle.as_view(), name='like-toggle'),


    url(r'^create/$', posts_create, name="create"),
	url(r'^(?P<slug>.+)/edit/$', posts_update, name='update'),
	url(r'^(?P<slug>.+)/$', posts_detail, name='detail'),
    url(r'^$', posts_list, name='list'),

    url(r'^(?P<slug>.+)/delete/$', post_delete, name='delete'),
    url(r'^search/$', posts_search, name="search"),

]
