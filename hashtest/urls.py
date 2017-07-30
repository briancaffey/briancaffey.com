from django.conf.urls import url, include
from hashtest import views
from hashtest.api.views import HashItemListAPIView, HashReferencingListAPIView
urlpatterns = [

		url(r'^$', views.hashitemtest, name="home"),

        url(r'^list/api/$', HashItemListAPIView.as_view(), name="hashitemlist"),

        url(r'^referencing-item-list/api/$', HashReferencingListAPIView.as_view(), name="hashitemreflist"),


]
