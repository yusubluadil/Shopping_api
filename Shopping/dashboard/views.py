from django.shortcuts import render, redirect
from mehsullar.models import Category, Product
from .forms import CategoryForm, ProductForm
# Create your views here.


def dashboard_panel(request):
  categories = Category.objects.all()
  products = Product.objects.all()

  context = {
    "categories" : categories,
    "products" : products,
  }

  return render(request, "dashboard.html", context)


def all_products(request):
  products = Product.objects.all()

  context = {
    "products" : products,
  }

  return render(request, "all_products.html", context)


def all_categories(request):
  categories = Category.objects.all()

  context = {
    "categories" : categories,
  }

  return render(request, "all_categories.html", context)


def create_category(request):
  form = CategoryForm()
  if (request.method == "POST"):
    form = CategoryForm(request.POST)

    if (form.is_valid()):
      form.save()
      return redirect("all_categories")
  
  context = {
    'form' : form
  }

  return render(request, 'create_category.html', context)


def create_product(request):
  form = ProductForm()
  if (request.method == "POST"):
    form = ProductForm(request.POST)

    if (form.is_valid()):
      form.save()
      return redirect("all_products")
  
  context = {
    'form' : form
  }

  return render(request, 'create_product.html', context) 

def delete_category(request, pk):
  category = Category.objects.get(pk = pk)
  category.delete()

  return redirect("all_categories")


def delete_product(request, pk):
  product = Product.objects.get(pk = pk)
  product.delete()

  return redirect("all_products")