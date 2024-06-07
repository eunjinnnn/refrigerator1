from django.db import models

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    img_url = models.URLField()

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    foodname = models.CharField(max_length=255)
    volume = models.IntegerField()
    unit = models.CharField(max_length=50)
    expiration_date = models.DateField()
    purchase_date = models.DateField()

    def __str__(self):
        return self.foodname