from django.shortcuts import render
from ventas.models import Venta
from django.views import generic
from ventas.forms import VentaForm
from django.urls import reverse_lazy
# Create your views here.
class ListarVentas(generic.ListView):
    model=Venta
    template_name="ventas/listar_ventas.html"
    context_object_name="cosa"
class InsertarVenta(generic.CreateView):
    model=Venta #Modelo de la vista
    template_name="ventas/insertar_venta.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=VentaForm #Formulario creado en django
    success_url=reverse_lazy("ventas:ventas_list") #Rediccionar luego de insertar
class EditarVenta(generic.UpdateView):
    model=Venta #Modelo de la vista
    template_name="ventas/insertar_venta.html" #Donde esta la plantilla
    context_object_name="cosa"
    form_class=VentaForm #Formulario creado en django
    success_url=reverse_lazy("ventas:ventas_list") #Rediccionar luego de insertar
class BorrarVenta(generic.DeleteView):
    model=Venta 
    template_name="ventas/borrar_venta.html" 
    context_object_name="cosa"
    form_class=VentaForm 
    success_url=reverse_lazy("ventas:ventas_list") 