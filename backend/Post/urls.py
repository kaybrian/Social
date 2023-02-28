from django.urls import path
from . import views


urlpatterns = [
    path('feed/', views.PostsView.as_view(), name="posts"),
    path('feed/<str:pk>/', views.PostDetailView.as_view(), name="post_details"),
    path('feed/<str:pk>/like/', views.LikePost.as_view(), name="like_post"),
    path('feed/<str:pk>/comments/',views.AddComment.as_view(), name='comments'),
]

