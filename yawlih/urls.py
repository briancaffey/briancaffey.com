from django.conf.urls import url
from .views import (
    yl_home,
    reports,
    user_logout,
    company_view,
)


urlpatterns = [

    url(r'^$', yl_home, name="home"),
    url(r'^reports/$', reports, name="reports"),
    url(r'^logout/$', user_logout, name="user_logout"),
    url(r'^company/(?P<id>\d+)/$', company_view, name="company_view")

]
