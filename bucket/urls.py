from django.urls import path
from bucket import views

app_name='bucket'
urlpatterns =[
    path('', views.bucket_list.as_view(), name='bucket'),
    path('create/', views.bucketCV.as_view(), name='create'),

]
