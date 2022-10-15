# from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    pass


# from caleb curry
@api_view(['GET'])
def drink_list(request):
    all_products = Product.objects.all()
    serializer = ProductSerializer(all_products, many=True)
    # return Response(serializer.data)
    return Response(serializer.data)
    
    