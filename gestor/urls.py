from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #publica/login/ir a registro
    path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('registro/', views.registro_view, name='registro_usuario'),
	path('registro-org/', views.registro_org_view, name='registro_organizacion'),
    path('inicio/', views.inicio, name='inicio'),
]
