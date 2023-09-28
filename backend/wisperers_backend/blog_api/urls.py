from django.urls import path
from .views import (
    ExtendedUserListCreateView,
    ExtendedUserDetailView,
    CategoryListCreateView,
    CategoryDetailView,
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
    CommentDetailView,
)

urlpatterns = [
    path('extendedusers/', ExtendedUserListCreateView.as_view(), name='extendeduser-list-create'),
    path('extendedusers/<int:pk>/', ExtendedUserDetailView.as_view(), name='extendeduser-detail'),
    
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    
    path('blogposts/', BlogPostListCreateView.as_view(), name='blogpost-list-create'),
    path('blogposts/<int:pk>/', BlogPostDetailView.as_view(), name='blogpost-detail'),
    
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
