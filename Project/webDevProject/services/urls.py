from django.urls import path
from services import views
from services.views import ServicesPageView, ServiceCreatePedido, PedidoSuccess


services_urlpatterns = ([
    path('', ServicesPageView.as_view(), name='services'),
    path('order/', views.realizar_pedido, name="detalle_pedido"),
    path('create_order', ServiceCreatePedido.as_view(), name='create_pedido'),
    path('success_order', PedidoSuccess.as_view(), name='success_pedido'),
], 'services')