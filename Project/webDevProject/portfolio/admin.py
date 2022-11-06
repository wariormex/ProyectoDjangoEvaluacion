from django.contrib import admin
from .models import Category, PortfolioItem, PortfolioItemImage

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

class PortfolioItemImageAdmin(admin.StackedInline):
    model = PortfolioItemImage
    

class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [PortfolioItemImageAdmin]
    
    readonly_fields = ('created','updated')
    ordering = ('published','title')
    search_fields = ('title',)
    
    date_hierarchy = 'published'
    list_filter = ('categories__name',)
    list_display = ('title','published', 'post_categories')
    
    class Meta:
        model = PortfolioItem
    
    def post_categories(self,obj):
        res = ""
        for c in obj.categories.all().order_by("name"):
            res += c.name + ", "
        res = res[0:len(res)-2]
        return res
    post_categories.short_description = "Categories"
  
class PortfolioItemImageAdmin(admin.ModelAdmin):
    pass
      
admin.site.register(Category, CategoryAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)
