# sales/urls.py

from django.urls import path
from .views import  crear_venta, historial_ventas, reportes

urlpatterns = [
    #path('', crear_venta, name='crear_venta'),
    path('crear/', crear_venta, name='crear_venta'),
    path('historial/', historial_ventas, name='historial_ventas'),
    path('reportes/', reportes, name='reportes'),
]
