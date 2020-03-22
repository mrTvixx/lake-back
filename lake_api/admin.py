from django.contrib import admin

from .models import Post, Comment, FileUpload


class FilesInline(admin.StackedInline):
    model = FileUpload
    extra = 0
    display_list = ('data_file')


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        FilesInline,
        CommentInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(FileUpload)
