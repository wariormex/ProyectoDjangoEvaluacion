"""webDevProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from . import settings
from core.urls import core_urlpatterns
from contact.urls import contact_urlpatterns
from portfolio.urls import portfolio_urlpatterns
from services.urls import services_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),
    path('services/', include(services_urlpatterns)),
    path('portfolio/', include(portfolio_urlpatterns)),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include(contact_urlpatterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



#Titulos Personalizados para el Admin
admin.site.site_header = "Moderna"
admin.site.index_title = "Administration Panel"
admin.site.site_title = 'My Site Admin'
admin.site.title = "Moderna"


    