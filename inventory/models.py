from django.db import models

class Shoe(models.Model):
    TIPO_GENERO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('U', 'Unisex'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    talla = models.DecimalField(max_digits=4, decimal_places=1)  # permite 42.5, 38.0, etc.
    color = models.CharField(max_length=30)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    genero = models.CharField(max_length=1, choices=TIPO_GENERO)
    fecha_ingreso = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - Talla {self.talla} ({self.color})"
