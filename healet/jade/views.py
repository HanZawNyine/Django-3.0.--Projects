from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage, Category, Comment, Profile
from .forms import CommentForm, ProductForm, ProductImagForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.text import slugify
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
import os


# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by('-created')[:8]
    return render(request, 'jade/home.html', {"latest_products": latest_products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    objects_list = Product.objects.all().order_by('-created')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        objects_list = objects_list.filter(category=category)

    paginator = Paginator(objects_list, 9)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "jade/products/product_list.html",
                  {"products": products, "categories": categories, "category": category})


def product_detail(request, year, month, day, slug):
    product = get_object_or_404(Product, slug=slug, created__year=year, created__month=month, created__day=day)
    return render(request, 'jade/products/product_detail.html', {"product": product})


def comments(request, year, month, day, slug):
    product = Product.objects.get(slug=slug)
    objects_list = product.product_comments.all().order_by('-created')
    comment_form = CommentForm()

    paginator = Paginator(objects_list, 3)
    page = request.GET.get('page')
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            form = comment_form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect('jade:comments', product.created.year, product.created.month, product.created.day,
                            product.slug)
    return render(request, 'jade/components/comments.html',
                  {"product": product, "comments": comments, "comment_form": comment_form})


def about(request):
    return render(request, 'jade/about/about.html')


def profile(request):
    user_profile = get_object_or_404(Profile, username=request.user)
    products = Product.objects.filter(author=request.user).order_by('-created')
    paginator = Paginator(products, 5)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'jade/about/profile.html', {'user_profile': user_profile, 'products': products})


def add_product(request):
    product_form = ProductForm()
    if request.method == 'POST':
        product_form = ProductForm(data=request.POST)
        images = request.FILES.getlist('images')
        if product_form.is_valid():
            prepare = product_form.save(commit=False)
            prepare.author = request.user
            prepare.slug = slugify(prepare.name)
            prepare.save()
            if images:
                for img in images:
                    product_image = ProductImage.objects.create(product=prepare, image=img)
                    product_image.save()
            return redirect('jade:profile')
    return render(request, 'jade/products/add_product.html', {"product_form": product_form})


def update_product(request, year, month, day, slug):
    product = get_object_or_404(Product, slug=slug, created__year=year, created__month=month, created__day=day)
    images = product.product_image.all()
    product_form = ProductForm(instance=product)
    ProductImageFOrm = modelformset_factory(ProductImage, form=ProductImagForm)
    product_image_form = ProductImageFOrm(queryset=images)
    if request.method == "POST":
        product_image_form = ProductImageFOrm(request.POST, request.FILES, queryset=images)
        # images.delete()
        product_image_form.save()
        product_form = ProductForm(request.POST, instance=product)
        images = request.FILES.getlist('images')
        if product_form.is_valid():
            prepare = product_form.save(commit=False)
            prepare.author = request.user
            prepare.slug = slugify(prepare.name)
            prepare.save()
            if images:
                for img in images:
                    product_image = ProductImage.objects.create(product=prepare, image=img)
                    product_image.save()

        return redirect('jade:profile')
    return render(request, 'jade/products/add_product.html',
                  {"product_form": product_form, "product_image_form": product_image_form})
