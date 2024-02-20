"""VASP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from home.views import home
from products.views import ProductListView,add_products
from orders.views import orders,add_orders
from home.views import login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('products/',ProductListView),
    path('home/products/',ProductListView),
    path('orders/',orders),
    path('',login),
    path('home/add',add_products,name='add_products'),
    path('home/adds',add_orders,name='add_orders'),
    path('home/orders/',orders)
   

 
   
    

]
