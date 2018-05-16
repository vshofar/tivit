from django.conf.urls import url
from feiras import views

urlpatterns = [
    url(r'^feira/$', views.feira_list),
    url(r'^feira/(?P<pk>[0-9]+)/$', views.feira_detail),
]
