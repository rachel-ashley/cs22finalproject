from django.urls import path, include
from . import views

app_name = 'webkiosk'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('',include('django.contrib.auth.urls'),name='login'),
    # food
    path('food/', views.listfood, name='food-list'),
    path('food/new/', views.createfood, name='food-create'),
    path('food/<int:pk>/', views.detailfood, name='food-detail'),
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),
    # customers
    path('customers/', views.listcustomers, name='customer-list'),
    path('customers/new/', views.createcustomer, name='customer-create'),
    path('customers/<int:pk>/', views.detailcustomer, name='customer-detail'),
    path('customers/<int:pk>/edit/', views.updatecustomer, name='customer-update'),
    path('customers/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),
    # Orders
    path('orders/', views.listorders, name='order-list'),
    path('orders/new/', views.createorder, name='order-create'),
    path('orders/<int:pk>/', views.detailorder, name='order-detail'),
    path('orders/<int:pk>/edit/', views.updateorder, name='order-update'),
    path('orders/<int:pk>/delete/', views.deleteorder, name='order-delete'),
]
