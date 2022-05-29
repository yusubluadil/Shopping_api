from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def index(request):
  categories = Category.objects.all()
  products = Product.objects.all()

  context = {
    'products' : products,
    'categories' : categories
  }
  return render(request, 'products.html', context)

def category_detail(request, pk):
  category = Category.objects.get(pk = pk)
  products = Product.objects.filter(category = category)
  categories = Category.objects.all()


  context = {
    'products' : products,
    'category' : category,
    'categories' : categories
  }
  return render(request, 'category.html', context)