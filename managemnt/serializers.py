from rest_framework import serializers
from .models import Profile, InventoryItem, ItemProfileMapping


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = ['user', 'type_of_user', 'belongs_to']



class InventoryItemSerializer(serializers.Serializer):
    class Meta:
        model = InventoryItem
        fields = ['name', 'belongs_to', 'availablity']



class ItemProfileMappingSerializer(serializers.Serializer):
    class Meta:
        model = ItemProfileMapping
        fields = ['profile', 'item']