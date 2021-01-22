from django.urls import path
from .views import (UserPostListView,
                    PostListView,
                    PostDetailView,
                    PostCreateView, PostUpdateView, PostDeleteView)


urlpatterns = [
    # Feedback paths
    path('feedback/', PostListView.as_view(), name='feedback'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('feedback/<int:pk>/', PostDetailView.as_view(), name='feedback-detail'),
    path('feedback/new/', PostCreateView.as_view(), name='feedback-create'),
    path('feedback/<int:pk>/update/', PostUpdateView.as_view(), name='feedback-update'),
    path('feedback/<int:pk>/delete/', PostDeleteView.as_view(), name='feedback-delete'),
]
