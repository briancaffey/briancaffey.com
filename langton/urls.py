from django.conf.urls import url, include
from langton import views

urlpatterns = [
    url(r'^$', views.main_view, name='main'),
    ]
