from django.shortcuts import render, get_object_or_404
from .models import Product, ProductImage, Category


# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by('-created')[:10]
    return render(request, 'jade/home.html', {"latest_products": latest_products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, "jade/products/product_list.html", {"products": products, "categories": categories,"category":category})


def product_detail(request, year, month, day, slug):
    product = get_object_or_404(Product, slug=slug, created__year=year, created__month=month, created__day=day)
    return render(request, 'jade/products/product_detail.html', {"product": product})


def about(request):
    return render(request, 'jade/about/about.html')
