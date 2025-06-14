from django.db import models
from django.conf import settings
from inventory.models import Shoe

class Sale(models.Model):
    vendedor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta #{self.id} - {self.vendedor.username} - {self.fecha.strftime('%Y-%m-%d')}"

class SaleDetail(models.Model):
    venta = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='detalles')
    zapato = models.ForeignKey(Shoe, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.zapato.nombre} (Venta #{self.venta.id})"
