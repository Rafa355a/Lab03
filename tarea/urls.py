from django.urls import path
from . import views

urlpatterns = [
    path('proveedores/', views.ProveedorListView.as_view(), name='proveedores_list'),
    path('proveedores/<int:pk>/', views.ProveedorDetailView.as_view(), name='proveedor_detail'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes_list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente_detail'),
    path('productos/', views.ProductoListView.as_view(), name='productos_list'),
    path('productos/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('ventas/', views.VentaListView.as_view(), name='ventas_list'),
    path('ventas/<int:pk>/', views.VentaDetailView.as_view(), name='venta_detail'),
]