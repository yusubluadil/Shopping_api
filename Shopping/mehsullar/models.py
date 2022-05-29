from django.db import models

# Create your models here.

class Category(models.Model):
  category_name = models.CharField(max_length = 100)

  def __str__(self):
    return self.category_name

class Product(models.Model):
  product_name = models.CharField(max_length = 500)
  product_description = models.CharField(max_length = 500)
  category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True)
  slug = models.SlugField()       #axtarisda id-i yox yazini gosterir.

  def __str__(self):
    return self.product_name