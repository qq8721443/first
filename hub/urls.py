
from django.urls import path
from hub.views import pageHub

app_name='hub'
urlpatterns = [
    path('', pageHub.as_view(), name='main')
]
