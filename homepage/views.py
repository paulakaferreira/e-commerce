from django.shortcuts import render
from catalog.models import Product

def home_page_view(request):
    products = Product.objects.all()  # Retrieve all products from the database
    return render(request, 'home.html', {'products': products})

