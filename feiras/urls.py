from django.conf.urls import url
from feiras import views
from django.urls import path

urlpatterns = [
    path(r'feira/', views.feira_list),
    path(r'feira/<str:registro>/', views.feira_detail),
]
