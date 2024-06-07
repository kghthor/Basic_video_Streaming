# videos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
]
