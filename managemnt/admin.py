from django.contrib import admin
from .models import Profile, InventoryItem, ItemProfileMapping

admin.site.register(Profile)
admin.site.register(InventoryItem)
admin.site.register(ItemProfileMapping)