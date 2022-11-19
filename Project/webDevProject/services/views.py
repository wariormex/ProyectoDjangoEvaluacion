from django.shortcuts import render
from django.views.generic.list import ListView
from services.models import Service

class ServicesPageView(ListView):
    model = Service
    paginate_by = 3
    template_name = 'services/services.html'
