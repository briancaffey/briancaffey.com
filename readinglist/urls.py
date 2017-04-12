from django.conf.urls import url
from .views import (
    reading_list,
    tag_view,
    all_tags,

)


urlpatterns = [

    url(r'^$', reading_list, name="list"),
    url(r'^tags/$', all_tags, name='all-tags'),
    url(r'^tags/(?P<slug>.+)/$', tag_view, name='tag-view'),


]
