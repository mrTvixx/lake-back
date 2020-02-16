from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostView(APIView):

    def get(self, request):
        response = Post.objects.all()
        serializer = PostSerializer(response, many=True)
        return Response(
            { "posts": serializer.data },
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        new_post = request.data
        serializer = PostSerializer(data=new_post)

        if serializer.is_valid(raise_exception=True):
            new_post_saved = serializer.save()

        return Response(
            {"success": "Article '{}' created successfully".format(new_post_saved.title)},
            status=status.HTTP_201_CREATED,
        )

class SinglePostView(APIView):

    def get(self, request, pk):
        response = Post.objects.filter(id=pk)

        if not len(response):
            return Response(status=status.HTTP_204_NO_CONTENT)

        serializer = PostSerializer(response[0])

        return Response(
            { "post": serializer.data },
            status=status.HTTP_200_OK,
        )


class CommentCreate(APIView):

    def post(self, request):
        new_comment = request.data
        serializer = CommentSerializer(data=new_comment)

        current_post = Post.objects.get(id=new_comment.get('post'))

        serializer.post = current_post

        if serializer.is_valid(raise_exception=True):
            print('SAVEEEEEEEEE')
            new_post_saved = serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class CommentView(APIView):

    def get(self, request, pk):
        current_post = Post.objects.get(id=pk)

        request = Comment.objects.filter(post=current_post)
        serializer = CommentSerializer(request, many=True)

        return Response(
            { "comments": serializer.data },
            status=status.HTTP_200_OK,
        )
