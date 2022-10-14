import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """DRF API VIEW""" 
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """DRF API VIEW"""
#     instance = Product.objects.all().order_by('title').first()
#     data = {}
#     if instance:
#         # data = model_to_dict(model_data)
#         data = ProductSerializer(instance).data
#     return Response(data)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """DRF API VIEW"""
#     print(request.data)
#     print(args)
#     print(kwargs)