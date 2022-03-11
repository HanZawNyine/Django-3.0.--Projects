from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500, unique_for_date='created')
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('jade:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique_for_date='created')
    category = models.ForeignKey(Category, models.CASCADE, related_name="product_category")
    price = models.IntegerField()
    description = models.TextField()
    author = models.ForeignKey(User, models.CASCADE, related_name="user_products")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jade:product_detail', args=[self.created.year, self.created.month, self.created.day, self.slug])

    def get_product_update_url(self):
        return reverse('jade:update_product', args=[self.created.year, self.created.month, self.created.day, self.slug])


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="product_image")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name="product_comments")
    user = models.ForeignKey(User, models.CASCADE, related_name="user_comments")
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


class Profile(models.Model):
    username = models.ForeignKey(User, models.CASCADE, related_name="user_profiles")
    phone_no = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='profiles/', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username.username
