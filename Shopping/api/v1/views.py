from rest_framework.response import Response
from mehsullar.models import Category, Product
from . serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(["GET", "POST"])
def products_list_create_api_view(request):
  if (request.method == "GET"):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many  = True)
    return Response(serializer.data)
  
  elif (request.method == "POST"):
    serializer = ProductSerializer(data = request.data)
    if (serializer.is_valid()):
      serializer.save()
      return Response(data = serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(status = status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def products_list_detail_api_view(request, pk):
  try:
    product_instance = Product.objects.get(pk = pk)
  except:
    return Response(
      {
        'errors' : {
          'code' : 404,
          'message' : f"{pk} id-li məhsul tapılmadı!"
        }
      },
      status = status.HTTP_404_NOT_FOUND
    )
    
  if (request.method == "GET"):
    serializer = ProductSerializer(product_instance)
    return Response(serializer.data)
  
  elif (request.method == "PUT"):
    serializer = ProductSerializer(product_instance, data = request.data, partial = True)
    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status = status.HTTP_200_OK)
    return Response(status = status.HTTP_400_BAD_REQUEST)
  
  elif (request.method == "DELETE"):
    product_instance.delete()
    return Response(
      {
        'errors' : {
          'code' : 204,
          'message' : f"{pk} id-li məhsul silindi."
        }
      },
      status = status.HTTP_204_NO_CONTENT
    )