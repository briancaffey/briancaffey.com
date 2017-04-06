from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home import views

urlpatterns = [

    url(r'^$', views.home, name='home')
]
