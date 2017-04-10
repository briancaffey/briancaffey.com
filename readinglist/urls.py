from django.conf.urls import url
from .views import (
    reading_list,
)


urlpatterns = [

    url(r'^$', reading_list, name="list"),

]
