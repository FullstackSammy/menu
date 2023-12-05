from django.urls import path
from .views import item_list, item_list_serialized, item_detail

urlpatterns = [
    path('', item_list, name='item-list'),
    path('drf/', item_list_serialized, name='item-list-drf'),
    path('<int:pk>/', item_detail),
]
