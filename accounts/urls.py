from django.conf.urls import url
from accounts.views import (
	login_view,
	register_view,
	logout_view,
)
from . import views


urlpatterns = [

    url(r'^login/$', login_view, name="login"),
	url(r'^logout/$', logout_view, name="logout"),
	url(r'^register/$', register_view, name="register"),

]
