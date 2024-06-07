from django.db import models
from django.forms import ValidationError
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.URLField()

    def __str__(self):
        return self.name

class FoodUnit(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=255)
    volume = models.IntegerField()
    unit = models.ForeignKey(FoodUnit, on_delete=models.CASCADE)
    expiration_date = models.DateField()
    purchase_date = models.DateField(default=timezone.now)  # Default 값으로 현재 날짜 사용

    def clean(self):
        if self.expiration_date < self.purchase_date:
            raise ValidationError("Expiration date must be after purchase date.")

    def __str__(self):
        return self.foodname
