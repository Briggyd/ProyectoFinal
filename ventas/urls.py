from django.urls import path
from ventas.views import ListarVentas, InsertarVenta,EditarVenta, BorrarVenta

urlpatterns = [
    path('ventas', ListarVentas.as_view(), name='ventas_list'),
    path('ventas/new', InsertarVenta.as_view(), name='insertar_venta'),
    path('ventas/edit<int:pk>', EditarVenta.as_view(), name='editar_venta'),
    path('ventas/delete<int:pk>', BorrarVenta.as_view(), name='borrar_venta'),
]