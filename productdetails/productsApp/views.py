from django.shortcuts import render

# Create your views here.


def electronics(request):
    prod_dict = {'product1': 'Mac', 'product2': 'iphone', 'product3': 'Dell'}
    return render(request, "Productapp/products.html", prod_dict)


def toy(request):
    prod_dict = {'product1': 'car', 'product2': 'doll', 'product3': 'bat'}
    return render(request, "Productapp/products.html", prod_dict)


def shoe(request):
    prod_dict = {'product1': 'Nike', 'product2': 'Puma', 'product3': 'adidas'}
    return render(request, "Productapp/products.html", prod_dict)


def index(request):
    return render(request, 'Productapp/index.html')
