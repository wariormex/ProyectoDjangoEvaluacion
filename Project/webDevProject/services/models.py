from django.db import models

class Service(models.Model):
    
    PAYMENT_MODELS = (
        ('Single Payment','Perpetual License'),
        ('Monthly Subscription','per Month'),
        ('Yearly Subscription','per Year'),
    )
    
    title= models.CharField(max_length=200, verbose_name="Title")
    price= models.FloatField(verbose_name="Price")
    payment= models.CharField(max_length=200, verbose_name="Contenido", choices=PAYMENT_MODELS) 
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ["price"]
        
    def __str__(self):
        return self.title
    
class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE, related_name='service_details')
    detail = models.CharField(max_length=500, verbose_name="Detail")
    
    def __str__(self):
        return self.service.title
    
class Pedido(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    email = models.EmailField(verbose_name="Email")
    name = models.CharField(max_length=100, verbose_name="Nombre")
    address = models.CharField(max_length=200, verbose_name="Calle y Numero")
    colony = models.CharField(max_length=200, verbose_name="Colonia")
    total = models.DecimalField(verbose_name="Total", max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["-date"]
    
    def __str__(self):
        return str(self.id)
