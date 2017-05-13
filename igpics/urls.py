from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import igpics


urlpatterns = [


    url(r'^$', igpics, name='igpics'),

]
