from django.conf.urls import url
from .views import (
    yl_home,
    reports,
)


urlpatterns = [

    url(r'^$', yl_home, name="home"),
    url(r'^reports/$', reports, name="reports"),


]
