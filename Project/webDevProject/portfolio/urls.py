from django.urls import path
from portfolio import views
from portfolio.views import PortfolioItemListView, PortfolioItemDetailView
from portfolio.views import PortfolioItemCreateView, PortfolioItemUpdateView, PortfolioItemDeleteView
#from django.contrib.auth import views as auth_views


portfolio_urlpatterns = ([
    path('', PortfolioItemListView.as_view(), name='portfolioitem_list'),
    path('detail/<pk>',PortfolioItemDetailView.as_view(), name='portfolioitem_detail'),
    path('create/', PortfolioItemCreateView.as_view(), name='create'),
    path('update/<pk>', PortfolioItemUpdateView.as_view(), name='update'),
    path('<pk>/delete/', PortfolioItemDeleteView.as_view(), name='delete'),
], 'portfolio')