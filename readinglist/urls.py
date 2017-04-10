from django.conf.urls import url
from .views import (
    reading_list,
    tag_view,
)


urlpatterns = [

    url(r'^$', reading_list, name="list"),
    url(r'^tags/(?P<id>.+)/$', tag_view, name='tag_view'),
    # url(r'^)


]
