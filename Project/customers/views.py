from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .forms import CustomerPreferenceForm

def create_preference(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = CustomerPreferenceForm(request.POST)
        if form.is_valid():
            preference = form.save(commit=False)
            preference.product = product  # link the product
            preference.save()
            return redirect("preference-success")
    else:
        form = CustomerPreferenceForm()

    return render(request, "customers/preference_form.html", {
        "form": form,
        "product": product,
    })


def preference_success(request):
    return render(request, "customers/preference_success.html")
