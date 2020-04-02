from django.urls import path
from .views import bucket_list

app_name='bucket'
urlpatterns =[
    path('', bucket_list.as_view(), name='bucket')
]
