from django.contrib import admin
from .models import Service, ServiceDetail

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class ServiceDetailAdmin(admin.StackedInline):
    model = ServiceDetail
    

class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailAdmin]
    
    readonly_fields = ('created','updated')
    ordering = ('updated','title')
    search_fields = ('title',)
    
    date_hierarchy = 'updated'
    list_display = ('title','updated',)
    
    class Meta:
        model = Service
  
class ServiceDetailAdmin(admin.ModelAdmin):
    pass
      
admin.site.register(Service, ServiceAdmin)
