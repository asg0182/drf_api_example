

from django.urls import path
from .views import PostListView, HealthCheck

urlpatterns = [
    path('', PostListView.as_view(), name='posts-list-api-view'),
    path('check/', HealthCheck.as_view(), name='health-check-api-view')
]