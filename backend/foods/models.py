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

# # 초기 데이터 정의
# initial_units = [
#     FoodUnit(name='개'),
#     FoodUnit(name='조각'),
#     FoodUnit(name='L'),
# ]

# initial_categories = [
#     Category(name='VEGETABLES'),
#     Category(name='DRINKS'),
#     Category(name='FROZEN_FOODS'),
#     Category(name='ETC'),
# ]

# # 초기 데이터를 한 번에 생성
# FoodUnit.objects.bulk_create(initial_units)
# Category.objects.bulk_create(initial_categories)