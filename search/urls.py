from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.search),
    url(r'^(\d+)',views.match)
]
