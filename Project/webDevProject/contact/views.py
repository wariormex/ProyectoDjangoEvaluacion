from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .forms import ContactForm
from django.urls import reverse_lazy
import time

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('name'))
            print(form.cleaned_data['email'])
            #return HttpResponseRedirect('/contact/thanks/')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})

def thanks(request):
    return render(request, 'contact/thanks.html')

def ejecutaAJAX(request):
    if request.method == "POST":
        opcion = request.POST.get('valor', '')
        respuesta = {}
        opciones = {}
        if opcion == '1':
            respuesta['estado'] = 'correcto'
            opciones['1'] = 'Aguascalientes'
            opciones['2'] = 'Chihuahua'
            opciones['3'] = 'CDMX'
            opciones['4'] = 'Querétaro'
            opciones['5'] = 'Yucatán'
        elif opcion == '2':
            respuesta['estado'] = 'correcto'
            opciones['1'] = 'California'
            opciones['2'] = 'Florida'
            opciones['3'] = 'Nueva York'
            opciones['4'] = 'Texas'
            opciones['5'] = 'Washington'
        else:
            respuesta['estado'] = 'No válido'
        respuesta['opciones'] = opciones
        time.sleep(1)
        return JsonResponse(respuesta)