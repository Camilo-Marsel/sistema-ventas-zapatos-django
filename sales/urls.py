from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('crear/', views.crear_venta, name='crear_venta'),
    path('historial_ventas/', views.historial_ventas, name='historial_ventas'),
    path('reportes/', views.reportes, name='reportes'),
]
