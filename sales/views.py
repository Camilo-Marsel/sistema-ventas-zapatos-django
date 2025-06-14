from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.contrib import messages
from .forms import SaleForm, SaleDetailFormSet
from .models import Sale, SaleDetail
from inventory.models import Shoe
from django.db.models import Sum, F
from django.db.models.functions import TruncDate

def es_vendedor_o_admin(user):
    return user.groups.filter(name__in=['Vendedor', 'Administrador']).exists()

@user_passes_test(es_vendedor_o_admin)
@login_required
@transaction.atomic
def crear_venta(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        formset = SaleDetailFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            # Validar stock antes de guardar
            for detalle_form in formset:
                if detalle_form.cleaned_data and not detalle_form.cleaned_data.get('DELETE', False):
                    zapato = detalle_form.cleaned_data['zapato']
                    cantidad = detalle_form.cleaned_data['cantidad']

                    if cantidad > zapato.cantidad:
                        messages.error(request, f"No hay suficiente inventario para {zapato.nombre}. Disponible: {zapato.cantidad}, solicitado: {cantidad}.")
                        return render(request, 'sales/crear_venta.html', {'form': form, 'formset': formset})

            # Guardar la venta
            venta = form.save(commit=False)
            venta.vendedor = request.user
            venta.total = 0
            venta.save()

            total = 0
            for detalle_form in formset:
                if detalle_form.cleaned_data and not detalle_form.cleaned_data.get('DELETE', False):
                    detalle = detalle_form.save(commit=False)
                    detalle.venta = venta
                    detalle.precio_unitario = detalle.zapato.precio
                    detalle.save()

                    # Actualizar inventario
                    detalle.zapato.cantidad -= detalle.cantidad
                    detalle.zapato.save()

                    total += detalle.cantidad * detalle.precio_unitario

            venta.total = total
            venta.save()
            messages.success(request, "Venta creada exitosamente.")
            return redirect('dashboard')
    else:
        form = SaleForm()
        formset = SaleDetailFormSet(queryset=SaleDetail.objects.none())

    return render(request, 'sales/crear_venta.html', {'form': form, 'formset': formset})

@login_required
def historial_ventas(request):
    ventas = Sale.objects.all()

    zapato_id = request.GET.get('zapato')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if zapato_id:
        ventas = ventas.filter(saledetail__zapato__id=zapato_id).distinct()

    if fecha_inicio:
        ventas = ventas.filter(fecha_venta__gte=fecha_inicio)

    if fecha_fin:
        ventas = ventas.filter(fecha_venta__lte=fecha_fin)

    zapatos = Shoe.objects.all()

    context = {
        'ventas': ventas,
        'zapatos': zapatos,
        'filtros': {
            'zapato_id': zapato_id,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
        }
    }
    return render(request, 'sales/historial_ventas.html', context)

@login_required
def reportes(request):
    # Reporte 1: Total vendido por día
    ventas_por_dia = (
        Sale.objects
        .annotate(fecha_anotada=TruncDate('fecha'))
        .values('fecha_anotada')
        .annotate(total_dia=Sum('total'))
        .order_by('-fecha_anotada')
    )

    # Reporte 2: Total vendido por producto
    ventas_por_producto = (
        SaleDetail.objects
        .values(nombre=F('zapato__nombre'))
        .annotate(total_vendido=Sum(F('cantidad') * F('precio_unitario')))
        .order_by('-total_vendido')
    )

    # Reporte 3: Total vendido por vendedor
    ventas_por_vendedor = (
        Sale.objects
        .values(nombre=F('vendedor__username'))
        .annotate(total_vendido=Sum('total'))
        .order_by('-total_vendido')
    )

    return render(request, 'sales/reportes.html', {
        'ventas_por_dia': ventas_por_dia,
        'ventas_por_producto': ventas_por_producto,
        'ventas_por_vendedor': ventas_por_vendedor,
    })
