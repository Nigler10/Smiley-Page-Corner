from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .forms import ProductForm

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_available=True)
    serializer_class = ProductSerializer


# Product List Page
def product_list(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'products/product_list.html', {'products': products})

# Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, is_available=True)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product-list-page")
    else:
        form = ProductForm()

    return render(request, "products/product_create.html", {
        "form": form
    })
