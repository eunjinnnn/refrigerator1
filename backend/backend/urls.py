from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ninja import NinjaAPI
from foods.api import router as foods_router

api = NinjaAPI()

api.add_router("/foods/", foods_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
