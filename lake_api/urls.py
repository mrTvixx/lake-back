from django.urls import path

from .views import PostView, SinglePostView, CommentView, CommentCreate, FileUploadViewSet

app_name="lake_api"

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:pk>', SinglePostView.as_view()),
    path('comments/', CommentCreate.as_view()),
    path('comments/<int:pk>', CommentView.as_view()),
    path('upload/', FileUploadViewSet.as_view()),
]