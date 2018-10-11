from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    text = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Video(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    video_title = models.CharField(max_length=300)
    video_url = models.URLField(max_length=500)

    def __str__(self):
        return self.video_title
