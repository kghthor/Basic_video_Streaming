# videos/forms.py

from django import forms
from django.conf import settings
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video 
        fields = ['title', 'video_file']

    def clean_video_file(self):
        video_file = self.cleaned_data.get('video_file')
        if video_file.size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(f"File size should be less than {settings.MAX_UPLOAD_SIZE / (1024 * 1024)} MB")
        return video_file
