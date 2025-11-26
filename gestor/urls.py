from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #publica/login/ir a registro
    path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('registro/', views.registro_view, name='registro_usuario'),
	path('registro_admin/', views.registro_admin_view, name='registro_organizacion'),
    path('inicio/', views.inicio, name='inicio'),
    path('cuotas/', views.cuotas_view, name='cuotas'),
    path('integrantes/', views.integrantes_view, name='integrantes'),
    path('pago_cuotas/', views.pago_cuotas_view, name='pago_cuotas'),
    path('registro_gasto/', views.registro_gasto_view, name='registro_gasto'),
    path('registro_item_gasto/<int:gasto_id>/', views.registro_item_gasto_view, name='registro_item_gasto'),
    path('gastos', views.lista_gastos_view, name='lista_gastos'),
    path('gastos/<int:gasto_id>/', views.detalle_gasto_view, name='detalle_gasto'),
]


