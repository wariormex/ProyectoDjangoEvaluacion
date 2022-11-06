from django.urls import path
from contact import views

contact_urlpatterns = ([
    path('', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('ejecutaAJAX/', views.ejecutaAJAX, name="ejecutaAJAX"),
], 'contact')