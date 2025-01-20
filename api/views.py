from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status	
from .models import Feed
from .serializer import FeedSerializer

@api_view(['GET'])
def get_feeds(request):
	feeds = Feed.objects.all()
	serializer = FeedSerializer(feeds, many=True)
	return Response(serializer.data)

@api_view(['GET','PUT', 'DELETE'])
def feed_detail(request, pk):
	try:
		feed = Feed.objects.get(pk=pk)
	except Feed.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = FeedSerializer(feed)
		return Response(serializer.data)
	elif request.method == 'PUT':
		serializer = FeedSerializer(feed, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	elif request.method == 'DELETE':
		feed.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def create_feed(request):
	serializer = FeedSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)