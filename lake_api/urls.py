from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import PostView, SinglePostView, CommentView, CommentCreate, FileUploadViewSet, PostsListView, SiteSettings

app_name = "lake_api"

urlpatterns = [
    path('settings/', SiteSettings.as_view()),
    path('posts/', PostsListView.as_view()),
    path('new_post/', csrf_exempt(PostView.as_view())),
    path('post/<int:pk>', SinglePostView.as_view()),
    path('comments/', csrf_exempt(CommentCreate.as_view())),
    path('comments/<int:pk>', CommentView.as_view()),
    path('upload/', FileUploadViewSet.as_view()),
]
