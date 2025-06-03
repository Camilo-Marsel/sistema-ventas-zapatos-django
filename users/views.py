from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    user = request.user
    roles = [group.name for group in user.groups.all()]

    contexto = {
        'es_admin': user.is_superuser,
        'es_vendedor': 'Vendedor' in roles,
        'es_inventario': 'Encargado Inventario' in roles,
    }
    return render(request, 'users/dashboard.html', contexto)
