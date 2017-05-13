from django.conf.urls import url
from .views import (
    graph_view,
    get_subreddits,
)


urlpatterns = [

    url(r'^$', graph_view, name="srgraph"),
    url(r'^api/get_drugs/', get_subreddits, name='get_subreddits'),




]
