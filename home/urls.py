from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from home import views
from home.views import CreateGuestBookAPIView

urlpatterns = [

    url(r'^gb-submit/', CreateGuestBookAPIView.as_view(), name='gb-submit'),
    url(r'^$', views.home, name='home'),
    url(r'^newsletter/confirm/(?P<uid>.+)/$', views.confirm_nl, name='confirm'),
    url(r'^newsletter/cancel/(?P<uid>.+)/$', views.cancel_nl, name='cancel'),

]
