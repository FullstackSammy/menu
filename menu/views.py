from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

from rest_framework.response import Response

from .serializers import ItemSerializer
from .models import Item

# Create your views here.

def item_list(request):
    items = Item.objects.all()
    item_list = []
    for item in items:
        item_list.append({
            'name': item.name,
            'prize': item.name,
            'description': item.description,
        })
    return JsonResponse({'menu': item_list})

def item_list_serialized(request):
    items = Item.objects.all()
    # Now we can serialize these using the serializer we just made
    serializer = ItemSerializer(items, many=True) #the serializer we just made. many is refering to if we have more than one item or not.
    return Response(serializer.data) # Using the sam JsonResponse class as before.

def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)