from django.conf.urls import url
from feiras import views
from django.urls import path

urlpatterns = [
    path(r'feira/', views.feira_list),
    path(r'feira/<str:registro>/', views.feira_detail),
    path(r'feira/distrito/<str:distrito>/', views.feira_list_distrito),
    path(r'feira/regiao5/<str:regiao5>/', views.feira_list_regiao5),
    path(r'feira/bairro/<str:bairro>/', views.feira_list_bairro),
    path(r'feira/nome-feira/<str:nome_feira>/', views.feira_list_nome_feira)
]
