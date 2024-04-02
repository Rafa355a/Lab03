from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Proveedor, Cliente, Producto, Venta

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedores_list.html'
    context_object_name = 'proveedores'

class ProveedorDetailView(DetailView):
    model = Proveedor
    template_name = 'proveedor_detail.html'
    context_object_name = 'proveedor'

class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'cliente_detail.html'
    context_object_name = 'cliente'

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto_detail.html'
    context_object_name = 'producto'

class VentaListView(ListView):
    model = Venta
    template_name = 'ventas_list.html'
    context_object_name = 'ventas'

class VentaDetailView(DetailView):
    model = Venta
    template_name = 'venta_detail.html'
    context_object_name = 'venta'