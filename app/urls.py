from django.urls import path
from .views import ProductListCreateView,ProductRetrieveUpdateDestroyView,ProductByNameView,UserRegisterView
urlpatterns = [
    path('products/',ProductListCreateView.as_view(),name='produc-list-create'),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroyView.as_view(),name='product-detail'),
    path('products/name/<str:name>/',ProductByNameView.as_view(),name='product-by-name'),
    path('register/',UserRegisterView.as_view(),name='register'),
    
]
