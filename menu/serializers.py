from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer): # Inherits from ModelSerializer since we're serializing a model.
    class Meta:
        model = Item # Specifierar vilken model vi vill serialize
        fields = '__all__' # Specifierar vilka fields vi vill serialize