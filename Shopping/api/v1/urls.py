from django.urls import path
from . import views


urlpatterns = [
  path('products/', views.products_list_create_api_view),
  path('products/<int:pk>', views.products_list_detail_api_view),
]