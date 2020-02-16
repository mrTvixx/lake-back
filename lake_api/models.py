from django.db import models
from django.utils import timezone
from datetime import datetime    

class Post(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    by_admin = models.BooleanField(default=True)
    create_date = models.DateTimeField(null=True)
    publish_date = models.DateTimeField(null=True)
    is_pablish = models.BooleanField(default=False)

    class Meta:
        ordering = ['publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    publish_date = models.DateTimeField(default=timezone.now(), blank=True)
    
    class Meta:
        ordering = ['publish_date']
