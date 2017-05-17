from django.conf.urls import url
from .views import (
    graph_view,
    get_subreddits,
    popular,
    view_result,
    upvote,
    downvote,
)


urlpatterns = [

    url(r'^$', graph_view, name="srgraph"),
    url(r'^(?P<id>\d+)/(?P<sbr1>[A-Za-z0-9_.]+)-and-(?P<sbr2>[A-Za-z0-9_.]+)/$', view_result, name="view_result"),
    url(r'^(?P<id>\d+)/$', view_result, name="view_result"),
    url(r'^(?P<id>\d+)/up/$', upvote, name="upvote"),
    url(r'^(?P<id>\d+)/down/$', downvote, name="downvote"),
    url(r'^popular/$', popular, name="popular"),

]
