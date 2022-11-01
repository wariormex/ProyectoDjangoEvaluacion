from django.urls import path
from core import views
#from django.contrib.auth import views as auth_views
from core.views import HomePageView


core_urlpatterns = ([
    path('', HomePageView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    
    #path('historia/', views.about, name='about'),
    #path('visitanos/', views.store, name='store'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
], 'core')