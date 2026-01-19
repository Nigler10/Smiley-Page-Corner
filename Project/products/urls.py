from django.urls import path
from .views import product_list, product_detail
from .views import ProductListAPIView, ProductDetailAPIView
from . import views

urlpatterns = [
    # Frontend pages
    path('', product_list, name='product-list-page'),
    path('<int:pk>/', product_detail, name='product-detail-page'),
    path("create/", views.product_create, name="product-create-page"),

    # API endpoints
    path("api/products/", ProductListAPIView.as_view(), name="product-list"),
    path("api/products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    
    
    path("cloudinary-test/", views.cloudinary_test, name="cloudinary-test"),
]
