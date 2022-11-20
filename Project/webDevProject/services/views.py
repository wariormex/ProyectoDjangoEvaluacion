from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from services.models import Service
from .forms import PedidoForm
from django.urls import reverse_lazy

class ServicesPageView(ListView):
    model = Service
    paginate_by = 3
    template_name = 'services/services.html'
    
class ServiceCreatePedido(CreateView):
    form_class = PedidoForm
    template_name = 'services/pedido_cliente.html'
    success_url = reverse_lazy('services:success_pedido')
    
    def form_valid(self, form):
        pedido_nuevo = form.save(commit=False)
        pedido_nuevo.save()
        return super().form_valid(form)
    
    def get_form_kwargs(self):
        kwargs = super(ServiceCreatePedido, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
class PedidoSuccess(TemplateView):
    template_name = 'services/pedido_success.html'

def _creaDiccionario(datos_pedido):
    diccionario = {}
    datos_pedido = datos_pedido[:-1]
    productos = datos_pedido.split('|')
    for producto in productos:
        detalle = producto.split('-')
        diccionario[detalle[0]] = int(detalle[1])
    return diccionario

def realizar_pedido(request):
    pedido = list()
    if request.method == 'POST':
        datos_pedido = request.POST['datos_pedido']
        print(datos_pedido)
        productos = _creaDiccionario(datos_pedido)
        total = 0
        for key in productos.keys():
            cantidad = productos[key]
            if cantidad > 0:
                dict_producto = {}
                servicio = Service.objects.get(pk=key)
                dict_producto['titulo'] = servicio.title
                dict_producto['modalidad'] = servicio.payment
                dict_producto['cantidad'] = cantidad
                dict_producto['precio'] = servicio.price
                dict_producto['subtotal'] = cantidad * servicio.price
                total += cantidad * servicio.price
                pedido.append(dict_producto)
        request.session['total_float'] = float(total)
        request.session['detalle_pedido'] = pedido
        print(pedido,total)
    return render(request, 'services/detalle_pedido.html',{"pedido":pedido, "total":total})               
         
 