from django.urls import path
from portfolio import views
from portfolio.views import PortfolioItemListView
#from django.contrib.auth import views as auth_views


portfolio_urlpatterns = ([
    path('', PortfolioItemListView.as_view(), name='portfolioitem_list'),
], 'portfolio')