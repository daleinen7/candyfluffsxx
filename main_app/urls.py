from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.ProductsList.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product_detail'),
    path('necahual', views.necahual, name='necahual'),
    path('accounts/signup/', views.signup, name='signup'),
]