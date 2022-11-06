from django.urls import path
from portfolio import views
from portfolio.views import PortfolioItemListView, PortfolioItemDetailView
#from django.contrib.auth import views as auth_views


portfolio_urlpatterns = ([
    path('', PortfolioItemListView.as_view(), name='portfolioitem_list'),
    path('detail/<pk>',PortfolioItemDetailView.as_view(), name='portfolioitem_detail'),
], 'portfolio')