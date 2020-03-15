from .models import Comment, Post, FileUpload
from rest_framework import serializers


class FileUploadSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    class Meta:
        model = FileUpload
        fields = '__all__'


class OnePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'by_admin', 'content', 'username')


class PostSerializer(serializers.ModelSerializer):
    files = FileUploadSerializer(many=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'by_admin', 'publish_date', 'is_publish', 'username', 'files', 'content')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
