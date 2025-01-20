from django.urls import path
from .views import create_feed, get_feeds, feed_detail

urlpatterns = [
	path('feeds/', get_feeds, name='get_feeds'),
	path('feeds/create/', create_feed, name='create_feed'),
	path('feeds/<int:pk>', feed_detail, name='feed_detail')
]