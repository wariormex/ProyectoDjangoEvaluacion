from django.shortcuts import render, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import PortfolioItem, PortfolioItemImage, Category
from .forms import PortfolioItemImageInlineFormSet, PortfolioItemImageInlineNoExtraFormSet

class PortfolioItemListView(ListView):
    model = PortfolioItem
    #paginate_by = 1
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class PortfolioItemDetailView(DetailView):
    model = PortfolioItem
    #template_name = "portfolioitem_detail.html"
    
class PortfolioItemCreateView(CreateView):
    model = PortfolioItem
    #fields = "__all__"
    fields = ['title', 'subtitle', 'content','categories','client', 'published','url']
    template_name_suffix = '_create_form'
    
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["children"] = PortfolioItemImageInlineFormSet(self.request.POST, self.request.FILES)
        else:
            data["children"] = PortfolioItemImageInlineFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children = context["children"]
        self.object = form.save()
        if children.is_valid():
            children.instance = self.object
            children.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portfolio:portfolioitem_list')
    
    #success_url = reverse_lazy('portfolio:portfolioitem_list')
    
    
class PortfolioItemUpdateView(UpdateView):
    model = PortfolioItem
    fields = ['title', 'subtitle', 'content','categories','client', 'published','url']
    template_name_suffix = '_update_form'
    
    def get_context_data(self, **kwargs):
        # we need to overwrite get_context_data
        # to make sure that our formset is rendered.
        # the difference with CreateView is that
        # on this view we pass instance argument
        # to the formset because we already have
        # the instance created
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["children"] = PortfolioItemImageInlineFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data["children"] = PortfolioItemImageInlineFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        children = context["children"]
        self.object = form.save()
        if children.is_valid():
            children.instance = self.object
            children.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('portfolio:portfolioitem_list')
    
    #success_url = reverse_lazy('portfolio:portfolioitem_list')
   
class PortfolioItemDeleteView(DeleteView):
    model = PortfolioItem
    template_name_suffix = '_delete_form'
    
    success_url = reverse_lazy('portfolio:portfolioitem_list')
