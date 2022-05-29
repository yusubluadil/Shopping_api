from django.urls import path
from dashboard import views

urlpatterns = [
  path('', views.dashboard_panel, name = "dashboard"),
  path('dashboard-all-products', views.all_products, name = "all_products"),
  path('dashboard-all-categories', views.all_categories, name = "all_categories"),
  path('create-category/', views.create_category, name = "create_category"),
  path('create-product/', views.create_product, name = "create_product"),
  path('delete-category/<int:pk>/', views.delete_category, name = "delete_category"),
  path('delete-product/<int:pk>/', views.delete_product, name = "delete_product"),
]