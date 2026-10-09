from django.db import models

class FoodItem(models.Model):
    item_id = models.CharField(max_length=20, primary_key=True)
    item_name = models.CharField(max_length=100)
    restaurant_name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=50)
    price = models.FloatField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.item_name} ({self.restaurant_name})"
