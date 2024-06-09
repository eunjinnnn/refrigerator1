from django.contrib import admin

from .models import Category, FoodUnit, FoodItem

admin.site.register(Category)
admin.site.register(FoodUnit)
admin.site.register(FoodItem)
