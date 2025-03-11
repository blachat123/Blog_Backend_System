from django.urls import path
from .views import RegisterUser, LoginUser, BlogListCreate, BlogDetailUpdateDelete, CommentListCreate

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('blogs/', BlogListCreate.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailUpdateDelete.as_view(), name='blog-detail-update-delete'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
]
