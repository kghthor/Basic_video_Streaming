# videos/views.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video
from .forms import VideoForm

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            return redirect(video.get_absolute_url())
    else:
        form = VideoForm()
    return render(request, 'videos/upload_video.html', {'form': form})

def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'videos/video_detail.html', {'video': video})
