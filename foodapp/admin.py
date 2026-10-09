from django.contrib import admin
from .models import FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'restaurant_name', 'cuisine', 'price', 'rating')
    search_fields = ('item_name', 'restaurant_name', 'cuisine')
    list_filter = ('cuisine', 'restaurant_name')

admin.site.register(FoodItem, FoodItemAdmin)
