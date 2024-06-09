from ninja import Router
from .models import Category, FoodItem, FoodUnit
from .schemas import CategorySchema, FoodItemSchema, FoodUnitSchema, VolumeUpdateSchema, FoodItemCreateSchema
from typing import List
from django.shortcuts import get_object_or_404
from ninja.errors import HttpError
import logging

router = Router()

# Set up logger
logger = logging.getLogger(__name__)

@router.get("/categories", response=List[CategorySchema])
def list_categories(request):
    return list(Category.objects.all())

@router.get("/foodunits", response=List[FoodUnitSchema])
def list_foodunits(request):
    return list(FoodUnit.objects.all())

@router.get("/fooditems", response=List[FoodItemSchema])
def list_fooditems(request):
    return list(FoodItem.objects.all())

@router.post("/fooditems", response=FoodItemSchema)
def create_fooditem(request, data: FoodItemCreateSchema):
    logger.info(f"Received data: {data}")  # 로그 추가
    try:
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
        logger.info(f"Food item created: {fooditem}")  # 생성된 항목 로그
        return fooditem
    except Exception as e:
        logger.error(f"Validation Error: {e}")
        raise HttpError(422, f"Validation Error: {e}")

# FoodItem 전체 수정
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

# FoodItem 삭제
@router.delete("/fooditems/{fooditem_id}", response={204: None})
def delete_fooditem(request, fooditem_id: int):
    fooditem = get_object_or_404(FoodItem, id=fooditem_id)
    fooditem.delete()
    return 204, None

# FoodItem volume 수정
@router.patch("/fooditems/{fooditem_id}/update_volume", response=FoodItemSchema)
def update_fooditem_volume(request, fooditem_id: int, data: VolumeUpdateSchema):
    fooditem = get_object_or_404(FoodItem, id=fooditem_id)
    new_volume = fooditem.volume + data.volume_change
    if new_volume < 0:
        raise HttpError(400, "Volume cannot be less than zero.")
    fooditem.volume = new_volume
    fooditem.save()
    return fooditem