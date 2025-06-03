# Listar zapato
from .forms import ShoeForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Shoe

def es_encargado(user):
    return user.groups.filter(name='Encargado de Inventario').exists() or user.is_superuser

@login_required
def lista_inventario(request):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')  # o algún mensaje

    zapatos = Shoe.objects.all().order_by('nombre')
    return render(request, 'inventory/lista_inventario.html', {'zapatos': zapatos})

# agregar zapato

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

# Eliminar zapato

@login_required
def eliminar_zapato(request, pk):
    if not es_encargado(request.user):
        return render(request, 'inventory/no_autorizado.html')

    zapato = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        zapato.delete()
        return redirect('lista_inventario')

    return render(request, 'inventory/eliminar_zapato.html', {'zapato': zapato})


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