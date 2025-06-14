# urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login y logout
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Dashboard
    path('', user_views.dashboard, name='dashboard'),

    # Puedes incluir otras rutas de tus apps
    path('inventario/', include('inventory.urls')),
    path('ventas/', include('sales.urls')),
]
