from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from django.forms.models import inlineformset_factory
from portfolio.models import PortfolioItem, PortfolioItemImage 


PortfolioItemImageInlineFormSet = inlineformset_factory(
    PortfolioItem,
    PortfolioItemImage,
    fields = ('images',),
    extra=3,
    )