from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.PostsView.as_view(), name="posts"),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name="post_details"),
    path('post/<str:pk>/like/', views.LikePost.as_view(), name="like_post"),
    path('post/<str:pk>/comments/',views.AddComment.as_view(), name='comments'),
    path('comment/<str:pk>/like/',views.LikeComment.as_view(), name='like_comments'),
    path('comment/<str:pk>/comments/',views.AddCommentToComment.as_view(), name="comment_on_comments"),

]

