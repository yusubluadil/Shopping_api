from django.urls import path
from mehsullar import views

urlpatterns = [
  path('', views.index, name = "index"),
  path('category/<int:pk>', views.category_detail, name = "category_detail")
]