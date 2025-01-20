from rest_framework.response import Response
from rest_framework import status	
from .models import Feed
from .serializer import FeedSerializer
from rest_framework.generics import GenericAPIView

class FeedsView(GenericAPIView):
	queryset = Feed.objects.all()
	serializer_class = FeedSerializer

	def get(self, request, *args, **kwargs):
		feeds = self.get_queryset()
		serializer = self.get_serializer(feeds, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, *args, **kwargs):
		feed = self.get_object()
		serializer = self.get_serializer(feed, data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		feed = self.get_object()
		feed.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)