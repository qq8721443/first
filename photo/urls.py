from django.urls import path
from .views import PhotoLV, PhotoDV, PhotologLV, PhotologDV, PhotologCV

app_name='photo'
urlpatterns = [
    path('', PhotologLV.as_view(), name='photolog_list'),
    path('list/<int:pk>/', PhotologDV.as_view(), name='photolog_detail'),
    path('create/', PhotologCV.as_view(), name='photolog_create'),

]
