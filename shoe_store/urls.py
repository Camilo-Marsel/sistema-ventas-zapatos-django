from django.contrib import admin
from django.urls import include, path
from users.views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('ventas/', include('sales.urls')),
    path('inventario/', include('inventory.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout routes default
    # Opción para ruta login personalizada:
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
