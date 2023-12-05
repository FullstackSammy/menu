from django.urls import path
from .views import item_list, item_list_serialized

urlpatterns = [
    path('', item_list_serialized, name='item-list')
]
