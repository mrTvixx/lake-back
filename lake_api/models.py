from django.db import models
from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=100, blank=True,
                             default='', verbose_name=u'')
    content = models.TextField(blank=True, verbose_name=u'Текст')
    by_admin = models.BooleanField(
        default=True, verbose_name=u'От имени админа')
    create_date = models.DateTimeField(
        null=True, verbose_name=u'Дата создания')
    publish_date = models.DateTimeField(
        null=True, blank=True, verbose_name=u'Дата публикации')
    is_publish = models.BooleanField(
        default=False, verbose_name=u'Опубликовано')
    username = models.CharField(
        blank=True, max_length=50, default='', verbose_name=u'Имя автора')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        if self.is_publish and not self.publish_date:
            self.publish_date = timezone.now()
        if self.username:
            self.by_admin = False
        self.modified = timezone.now()
        return super(Post, self).save(*args, **kwargs)


class FileUpload(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, to_field='id', on_delete=models.CASCADE, verbose_name=u'Название поста', related_name='files')
    data_file = models.FileField(verbose_name=u'Файл')


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, to_field='id', related_name='comments')
    content = models.CharField(max_length=2500)
    publish_date = models.DateTimeField(default=timezone.now(), blank=True)
    by_admin = models.BooleanField(
        default=True, blank=True, verbose_name=u'От имени админа')
    username = models.CharField(
        blank=True, max_length=50, default='', verbose_name=u'Имя автора')

    class Meta:
        ordering = ['publish_date']

    def save(self, *args, **kwargs):
        if self.username:
            self.by_admin = False
        self.publish_date = timezone.now()
        self.modified = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
