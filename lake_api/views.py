from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics

from .models import Post, Comment, FileUpload
from .serializers import PostSerializer, CommentSerializer, FileUploadSerializer, OnePostSerializer


class CustomPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.num_pages,
            'results': data
        })


class FileUploadViewSet(APIView):
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request):
        response = request.data
        serializer = FileUploadSerializer(data=response)

        current_post = Post.objects.get(id=response.get('post'))
        serializer.post = current_post

        if serializer.is_valid():
            new_file = serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class PostsListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_publish=True).order_by('-publish_date')
    serializer_class = PostSerializer
    pagination_class = CustomPagination


class PostView(APIView):
    def post(self, request):
        new_post = request.data
        serializer = OnePostSerializer(data=new_post)

        if serializer.is_valid(raise_exception=True):
            new_post_saved = serializer.save()

        return Response(
            {"id": new_post_saved.id},
            status=status.HTTP_201_CREATED,
        )


class SinglePostView(APIView):

    def get(self, request, pk):
        response = Post.objects.filter(id=pk)
        files = FileUpload.objects.filter(post=pk)

        if not len(response):
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = PostSerializer(response[0])
        serializer_files = FileUploadSerializer(files, many=True)

        return Response(
            {"post": serializer.data},
            status=status.HTTP_200_OK,
        )


class CommentCreate(APIView):

    def post(self, request):
        response = request.data
        serializer = CommentSerializer(data=response)

        current_post = Post.objects.get(id=response.get('post'))
        serializer.post = current_post

        if serializer.is_valid():
            new_post_saved = serializer.save()

        comments = Comment.objects.filter(post=current_post)
        serializer_comments = CommentSerializer(comments, many=True)

        return Response({
            'data': serializer_comments.data,
        }, status=status.HTTP_201_CREATED)


class CommentView(APIView):

    def get(self, request, pk):
        current_post = Post.objects.get(id=pk)

        request = Comment.objects.filter(post=current_post)
        serializer = CommentSerializer(request, many=True)

        return Response(
            {"comments": serializer.data},
            status=status.HTTP_200_OK,
        )
