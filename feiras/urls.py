from django.conf.urls import url
from feiras import views

urlpatterns = [
    url(r'^feiras/$', views.feira_list),
    url(r'^feiras/(?P<pk>[0-9]+)/$', views.feira_detail),
]
