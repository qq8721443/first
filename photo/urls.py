from django.urls import path
from .views import PhotoLV, PhotoDV

app_name='photo'
urlpatterns = [
    path('', PhotoLV.as_view(), name='photo_list'),
    path('list/<int:pk>/', PhotoDV.as_view(), name='photo_detail'),
]
