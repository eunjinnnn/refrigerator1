from ninja import Schema
from datetime import date
from typing import Optional

class CategorySchema(Schema):
    id: Optional[int]
    name: str
    img_url: str

class FoodUnitSchema(Schema):
    id: Optional[int]
    name: str

class FoodItemSchema(Schema):
    category_id: int
    foodname: str
    volume: int
    unit_id: int
    expiration_date: date
    purchase_date: date

class VolumeUpdateSchema(Schema):
    volume_change: int

# class FoodItemCreateSchema(Schema):
#     category: int
#     foodname: str
#     volume: int
#     unit: int
#     expiration_date: date
#     purchase_date: date

# class FoodItemUpdateSchema(Schema):
#     category: int
#     foodname: str
#     volume: int
#     unit: int
#     expiration_date: date
#     purchase_date: date

# class FoodItemVolumeUpdateSchema(Schema):
#     volume: int