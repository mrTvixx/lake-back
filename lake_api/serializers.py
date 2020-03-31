from .models import Comment, Post, FileUpload, FilterWord
from rest_framework import serializers


class SettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilterWord
        fields = ['word']


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    files = FileUploadSerializer(many=True)
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'by_admin', 'publish_date', 'comments',
                  'is_publish', 'username', 'files', 'content')
