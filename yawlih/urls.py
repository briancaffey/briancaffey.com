from django.conf.urls import url
from .views import (
    yl_home,
    reports,
    user_logout,
    company_view,
    advanced_search,
)


urlpatterns = [
    url(r'^search/$', advanced_search, name="advanced_search"),
    url(r'^$', yl_home, name="home"),
    url(r'^logout/$', user_logout, name="user_logout"),
    url(r'^company/(?P<id>\d+)/$', company_view, name="company_view"),
]
