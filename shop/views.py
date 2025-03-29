from django.shortcuts import render
from .models import Category, Product

def home(request):
    featured_products = Product.objects.filter(is_featured=True)
    context = {
        'featured_products': featured_products,
        'show_footer': True
    }
    return render(request, 'home.html', context)

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop.html', {'categories': categories, 'products': products})

def category_products(request, category):
    category_obj = Category.objects.get(name=category)
    products = Product.objects.filter(category=category_obj)
    return render(request, 'category_products.html', {'category': category_obj, 'products': products})

def faq():
    print("Will be handled!")

def cart():
    print("Will be handled!")