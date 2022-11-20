from django.shortcuts import render
from django.views.generic.list import ListView
from services.models import Service

class ServicesPageView(ListView):
    model = Service
    paginate_by = 3
    template_name = 'services/services.html'

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
         
 