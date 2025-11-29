from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), #publica/login/ir a registro
    # login
    path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
    # registro
	path('registro/', views.registro_view, name='registro_usuario'),
	path('registro_admin/', views.registro_admin_view, name='registro_organizacion'),
    # inicio
    path('inicio/', views.inicio, name='inicio'),
    # cuotas
    path('cuotas/', views.cuotas_view, name='cuotas'),
    path('pago_cuotas/', views.pago_cuotas_view, name='pago_cuotas'),
    path('cuotas/lista', views.lista_cuotas_view, name='lista_cuotas'),
    path('cuotas/<int:cuota_id>/eliminar/', views.confirmar_eliminar_cuota_view, name='confirmar_eliminar_cuota'),
    path('cuotas/<int:cuota_id>/eliminar/confirmado', views.eliminar_cuota, name='eliminar_cuota'),
    # integrantes
    path('integrantes/', views.integrantes_view, name='integrantes'),
    path('integrantes/<int:integrante_id>/eliminar/', views.confirmar_eliminar_integrante_view, name='confirmar_eliminar_integrante'),
    path('integrantes/<int:integrante_id>/eliminar/confirmado', views.eliminar_integrante, name='eliminar_integrante'),
    path('integrantes/editar/', views.editar_integrante_view, name='editar_integrante'),
    path('perfil/', views.perfil_integrante_view, name='perfil_integrante'),
    # gastos
    path('registro_gasto/', views.registro_gasto_view, name='registro_gasto'),
    path('registro_item_gasto/<int:gasto_id>/', views.registro_item_gasto_view, name='registro_item_gasto'),
    path('gastos', views.lista_gastos_view, name='lista_gastos'),
    path('gastos/<int:gasto_id>/', views.detalle_gasto_view, name='detalle_gasto'),
    path('gastos/<int:gasto_id>/eliminar/', views.confirmar_eliminar_gasto_view, name='confirmar_eliminar_gasto'),
    path('gastos/<int:gasto_id>/eliminar/confirmado/', views.eliminar_gasto, name='eliminar_gasto'),
]


