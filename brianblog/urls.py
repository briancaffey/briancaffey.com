"""brianblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from posts import views
from comments.views import CommentCreateAPIView


urlpatterns = [
    url(r'^users/', include('friends.urls', namespace="friends")),
    url(r'^ig/', include('igpics.urls', namespace="igpics")),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('posts.urls', namespace="posts")),
    url(r'^api/blog/', include('posts.api.urls', namespace="posts")),
    url(r'^api/blog/(?P<slug>.+)/comment/$', CommentCreateAPIView.as_view(), name="api-add-comment"),
    url(r'^', include('home.urls', namespace="home" )),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^comments/', include('comments.urls', namespace='comments')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^readinglist/', include('readinglist.urls', namespace='reading-list')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
