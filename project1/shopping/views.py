from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'all_items/':'/',
        'Add':'/create',
        'Update':'/update/pk',
        'Delete':'/item/pk/delete',

    }
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item=ProductSerializer(data=request.data)
    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_items(request):
    if request.query_params:
        items=Product.objects.filter(**request.query_params.dict())

    else:
        items=Product.objects.all()

    if items:
        data=ProductSerializer(items, many=True)
        return Response(data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_items(request,pk):
    item=Product.objects.get(pk=pk)
    data=ProductSerializer(instance=item,data=request.data)

    if data.is_valid():
        data.save()
        return Response(data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)








