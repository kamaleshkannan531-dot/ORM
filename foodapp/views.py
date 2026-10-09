from django.shortcuts import render
from .models import FoodItem

def food_list(request):
    items = FoodItem.objects.all()
    return render(request, 'foodapp/index.html', {'items': items})
