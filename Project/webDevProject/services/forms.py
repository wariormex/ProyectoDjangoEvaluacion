from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from services.models import Service, Pedido 

class PedidoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        total_float = self.request.session.get('total_float')
        super().__init__(*args, **kwargs)
        self.fields["total"].initial=total_float
        
    class Meta:
        model = Pedido
        fields = ['name', 'address', 'colony', 'email', 'total']
        widgets = {
            'name':TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'address':TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'colony':TextInput(attrs={'class':'form-control', 'placeholder':'Colony'}),
            'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }