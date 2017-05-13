from django.conf.urls import url
from .views import (
    graph_view,
)


urlpatterns = [

    url(r'^$', graph_view, name="srgraph"),




]
