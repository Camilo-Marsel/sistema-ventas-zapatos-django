from django.db import models
from django.conf import settings
from inventory.models import Shoe

class Sale(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta #{self.id} - {self.vendedor.username} - {self.fecha.date()}"


class SaleDetail(models.Model):
    venta = models.ForeignKey(Sale, related_name='detalles', on_delete=models.CASCADE)
    zapato = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.zapato.nombre}"
