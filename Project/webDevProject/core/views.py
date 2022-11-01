from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = 'core/home.html'

#def home(request):
#    return render(request,'core/home.html')

#def blog(request):
#    return render(request,'core/blog.html')
