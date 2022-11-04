from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modification Date")
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class PortfolioItem(models.Model):
    title= models.CharField(max_length=200, verbose_name="Title")
    #Multiple images
    #image = models.FileField(blank=True)
    #Project Information
    subtitle= models.CharField(max_length=200, verbose_name="Subtitle")
    content = RichTextUploadingField(verbose_name="Content")
    #Project Details
    categories = models.ManyToManyField(Category,verbose_name="Categories", related_name="get_portfolio_items")
    client= models.CharField(max_length=200, verbose_name="Client")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicacion")
    url = models.URLField(max_length=200, verbose_name="URL")
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated = models.DateTimeField(auto_now=True, verbose_name="Modification Date")
    
    class Meta:
        verbose_name = "Portolio Item"
        verbose_name_plural = "Portolio Items"
        ordering = ["-updated"]
        
    def __str__(self):
        return self.title
    
class PortfolioItemImage(models.Model):
    portfolioItem = models.ForeignKey(PortfolioItem, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = "portfolio")
    
    def __str__(self):
        return self.portfolioItem.title
