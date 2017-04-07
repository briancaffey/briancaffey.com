from django.conf.urls import url
from posts.views import (
	posts_create, 
	posts_list, 
	posts_update, 
	post_delete,
	posts_detail, 
	posts_search,
)


urlpatterns = [

    url(r'^create/$', posts_create, name="create"),
    url(r'^$', posts_list, name='list'),
    url(r'^(?P<slug>.+)/edit/$', posts_update, name='update'),
    url(r'^(?P<slug>.+)/delete/$', post_delete),
    url(r'^(?P<slug>.+)/$', posts_detail, name='detail'),
    url(r'^search/$', posts_search, name="search"),

]