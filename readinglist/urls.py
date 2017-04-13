from django.conf.urls import url
from .views import (
    reading_list,
    tag_view,
    all_tags,
    delete,
    edit,
    view_item,

)


urlpatterns = [

    url(r'^$', reading_list, name="list"),
    url(r'^tags/$', all_tags, name='all-tags'),
    url(r'^tags/(?P<slug>.+)/$', tag_view, name='tag-view'),
    url(r'^(?P<pk>[0-9]+)/delete/$', delete, name='delete'),
    url(r'^(?P<pk>[0-9]+)/edit/$', edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/$', view_item, name='view-item'),



]
