from django.urls import path, re_path
from Post import views

app_name = 'post'
urlpatterns = [
    path('', views.PostLV.as_view(), name='post_list'),
    path('create/', views.PostCV.as_view(), name='post_create'),
    re_path(r'^test/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'),
    path('<int:pk>/update/', views.PostUV.as_view(),name='post_update'),
    path('<int:pk>/delete/',views.PostDelV.as_view(), name='post_delete'),
]
