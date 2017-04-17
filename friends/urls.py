from django.conf.urls import url, include

from friends.views import (

    friend_list,
    add_or_remove_friends,
)


urlpatterns = [
    url(r'^$', friend_list, name="friend-list"),

    url(r'^connect/(?P<verb>.+)/(?P<username>.+)/$', add_or_remove_friends, name="add_or_remove_friends")
]
