from django.db import models
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    by_admin = models.BooleanField(default=True)
    create_date = models.DateTimeField(null=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    is_publish = models.BooleanField(default=False)
    username = models.CharField(blank=True, max_length=50, default='')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        if self.is_publish and not self.publish_date:
            self.publish_date = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, to_field='id', on_delete=models.CASCADE, related_name='files')
    data_file = models.FileField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    publish_date = models.DateTimeField(default=timezone.now(), blank=True)

    class Meta:
        ordering = ['publish_date']
