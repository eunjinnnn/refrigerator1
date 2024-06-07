# foods/api.py

from ninja import Router
from .models import Category, FoodItem, FoodUnit
from .schemas import CategorySchema, FoodItemSchema, FoodUnitSchema, VolumeUpdateSchema
from typing import List
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError

router = Router()
#cat, unit, food 전체 조회
@router.get("/categories", response=List[CategorySchema])
def list_categories(request):
    return list(Category.objects.all())

@router.get("/foodunits", response=List[FoodUnitSchema])
def list_foodunits(request):
    return list(FoodUnit.objects.all())

@router.get("/fooditems", response=List[FoodItemSchema])
def list_fooditems(request):
    return list(FoodItem.objects.all())

#food등록
@router.post("/fooditems", response=FoodItemSchema)
def create_fooditem(request, data: FoodItemSchema):
    category = get_object_or_404(Category, id=data.category_id)
    unit = get_object_or_404(FoodUnit, id=data.unit_id)
    fooditem = FoodItem.objects.create(
        category=category,
        foodname=data.foodname,
        volume=data.volume,
        unit=unit,
        expiration_date=data.expiration_date,
        purchase_date=data.purchase_date
    )
    return fooditem

#food 전체 수정
@router.put("/fooditems/{fooditem_id}", response=FoodItemSchema)
def update_fooditem(request, fooditem_id: int, data: FoodItemSchema):
    fooditem = get_object_or_404(FoodItem, id=fooditem_id)
    fooditem.category = get_object_or_404(Category, id=data.category_id)
    fooditem.foodname = data.foodname
    fooditem.volume = data.volume
    fooditem.unit = get_object_or_404(FoodUnit, id=data.unit_id)
    fooditem.expiration_date = data.expiration_date
    fooditem.purchase_date = data.purchase_date
    fooditem.save()
    return fooditem

#food 삭제
@router.delete("/fooditems/{fooditem_id}", response={204: None})
def delete_fooditem(request, fooditem_id: int):
    fooditem = get_object_or_404(FoodItem, id=fooditem_id)
    fooditem.delete()
    return 204, None

#volume 수정
@router.patch("/fooditems/{fooditem_id}/update_volume", response=FoodItemSchema)
def update_fooditem_volume(request, fooditem_id: int, data: VolumeUpdateSchema):
    fooditem = get_object_or_404(FoodItem, id=fooditem_id)
    new_volume = fooditem.volume + data.volume_change
    if new_volume < 0:
        raise HttpError(400, "Volume cannot be less than zero.")
    fooditem.volume = new_volume
    fooditem.save()
    return fooditem
