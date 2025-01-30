from django.urls import path  # Import path để định nghĩa URL
from .views import (PostListView, 
                    PostDetailView, 
                    PostCreateView,
                    PostUpdateView, 
                    PostDeleteView,
                    UserPostListView, # Import các view từ views.py
                    UserProfileView, 
                    like_post,
                    comment_post,
                    # user_profile_view,

                     ) # Import các view cần sử dụng

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'), 
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),     # URL chi tiết bài viết, với 'pk' là primary key của bài viết, gọi tên là 'post-detail'
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # URL tạo bài viết mới, gọi tên là 'post-create'
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete',  PostDeleteView.as_view(), name='post-delete'),   
    
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile-view'),  # Thêm URL mới
    path('post/<int:pk>/like/', like_post, name='like-post'),
    path('post/<int:pk>/comment/', comment_post, name='comment-post'),
 
]   
