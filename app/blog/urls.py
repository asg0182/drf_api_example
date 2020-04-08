from django.urls import path, include
from .views import current_datetime, PostListView, PostDetailVIew

urlpatterns = [
    path('api/', include('blog.api.urls')),
    path('now/', current_datetime, name='now-blog-view'),
    path('posts/', PostListView.as_view(), name='posts-list-view'),
    path('detail/<pk>', PostDetailVIew.as_view(), name='post-detail-view'),
]