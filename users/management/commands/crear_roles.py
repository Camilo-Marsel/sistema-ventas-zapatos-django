from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from inventory.models import Shoe
from sales.models import Sale, SaleDetail

class Command(BaseCommand):
    help = 'Crea grupos y asigna permisos por rol'

    def handle(self, *args, **kwargs):
        # 1. Vendedor
        vendedor, created = Group.objects.get_or_create(name='Vendedor')
        permisos_venta = Permission.objects.filter(content_type__model='sale')
        vendedor.permissions.set(permisos_venta)

        # 2. Encargado Inventario
        encargado, created = Group.objects.get_or_create(name='Encargado Inventario')
        permisos_inventario = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Shoe))
        encargado.permissions.set(permisos_inventario)

        # 3. Administrador (opcional, si no usas superusuarios)
        admin, created = Group.objects.get_or_create(name='Administrador')
        todos_los_permisos = Permission.objects.all()
        admin.permissions.set(todos_los_permisos)

        self.stdout.write(self.style.SUCCESS('Grupos creados y permisos asignados correctamente.'))
