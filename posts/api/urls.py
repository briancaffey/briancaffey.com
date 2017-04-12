from django.conf.urls import url
from .views import (
    PostListAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostCreateAPIView,
)

urlpatterns = [
    url(r'^create/$', PostCreateAPIView.as_view(), name='create'),
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='edit'),
    url(r'^(?P<slug>[\w-]+÷)/delete/$', PostDeleteAPIView.as_view(), name='delete'),





]
