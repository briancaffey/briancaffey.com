from django.conf.urls import url
from .views import (
    graph_view,
    get_subreddits,
)


urlpatterns = [

    url(r'^$', graph_view, name="srgraph"),

]
