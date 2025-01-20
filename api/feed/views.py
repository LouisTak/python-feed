from rest_framework.response import Response
from rest_framework import status	
from .models import Feed
from .serializer import FeedSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FeedListCreateView(generics.ListCreateAPIView):
	queryset = Feed.objects.all()
	serializer_class = FeedSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	@swagger_auto_schema(
		operation_summary="List all feeds or create a new feed",
		operation_description="Get a list of all feeds or create a new one. Authentication required for creation.",
		request_body=FeedSerializer,
		responses={
			201: openapi.Response(
				description="Feed created successfully",
				schema=FeedSerializer
			)
		}
	)
	def get_serializer_context(self):
		context = super().get_serializer_context()
		return context

	def perform_create(self, serializer):
		serializer.save()

class FeedDetailView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Feed.objects.all()
	serializer_class = FeedSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	@swagger_auto_schema(
		operation_summary="Retrieve, update or delete a feed",
		operation_description="Get, update or delete a specific feed. Authentication required for update and delete."
	)
	def perform_update(self, serializer):
		# Ensure only the author can update their own feeds
		if serializer.instance.author != self.request.user:
			raise PermissionError("You can only update your own feeds")
		serializer.save()

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		# Ensure only the author can delete their own feeds
		if instance.author != request.user:
			raise PermissionError("You can only delete your own feeds")
		return super().destroy(request, *args, **kwargs)