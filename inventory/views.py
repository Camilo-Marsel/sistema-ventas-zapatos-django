# Listar zapato
from .forms import ShoeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Shoe

# 🚩 Función corregida: usar el campo `role` correctamente
def es_encargado(user):
    return user.role == 'inventario' or user.is_superuser

# 🚩 Lista de inventario
@login_required
def lista_inventario(request):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')

    zapatos = Shoe.objects.all().order_by('nombre')
    return render(request, 'inventory/lista_inventario.html', {'zapatos': zapatos})

# 🚩 Agregar zapato
@login_required
def agregar_zapato(request):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')

    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_inventario')
    else:
        form = ShoeForm()
    return render(request, 'inventory/agregar_zapato.html', {'form': form})

# 🚩 Eliminar zapato
@login_required
def eliminar_zapato(request, pk):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')

    zapato = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        zapato.delete()
        return redirect('lista_inventario')

    return render(request, 'inventory/eliminar_zapato.html', {'zapato': zapato})

# 🚩 Actualizar zapato
@login_required
def actualizar_zapato(request, pk):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')

    zapato = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        form = ShoeForm(request.POST, instance=zapato)
        if form.is_valid():
            form.save()
            return redirect('lista_inventario')
    else:
        form = ShoeForm(instance=zapato)

    return render(request, 'inventory/actualizar_zapato.html', {'form': form, 'zapato': zapato})
