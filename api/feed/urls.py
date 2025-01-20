from django.urls import path
from .views import FeedListCreateView, FeedDetailView

urlpatterns = [
	path('feeds/', FeedListCreateView.as_view(), name='feed-list-create'),
	path('feeds/<int:pk>/', FeedDetailView.as_view(), name='feed-detail'),
]