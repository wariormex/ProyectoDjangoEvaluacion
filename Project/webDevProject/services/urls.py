from django.urls import path
from services.views import ServicesPageView


services_urlpatterns = ([
    path('', ServicesPageView.as_view(), name='services'),
], 'services')