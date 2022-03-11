from .models import Comment, Product, ProductImage
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'description')


class ProductImagForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)
