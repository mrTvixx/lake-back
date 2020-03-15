from django.urls import path

from .views import PostView, SinglePostView, CommentView, CommentCreate, FileUploadViewSet, PostsListView

app_name = "lake_api"

urlpatterns = [
    path('posts/', PostsListView.as_view()),
    path('new_post/', PostView.as_view()),
    path('post/<int:pk>', SinglePostView.as_view()),
    path('comments/', CommentCreate.as_view()),
    path('comments/<int:pk>', CommentView.as_view()),
    path('upload/', FileUploadViewSet.as_view()),
]
