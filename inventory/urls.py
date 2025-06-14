from django.urls import path
from .views import actualizar_zapato, lista_inventario, agregar_zapato, eliminar_zapato

app_name = 'inventory'

urlpatterns = [
    path('', lista_inventario, name='lista_inventario'),
    path('agregar/', agregar_zapato, name='agregar_zapato'),
    path('eliminar/<int:pk>/', eliminar_zapato, name='eliminar_zapato'),
    path('actualizar/<int:pk>/', actualizar_zapato, name='actualizar_zapato'),
]
