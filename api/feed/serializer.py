from rest_framework import serializers
from .models import Feed
from api.users.serializer import UserSerializer

class FeedSerializer(serializers.ModelSerializer):
	author = UserSerializer(read_only=True)

	class Meta:
		model = Feed
		fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']
		read_only_fields = ['created_at', 'updated_at', 'author']

	def create(self, validated_data):
		# Get the author from the context (will be set in the view)
		author = self.context.get('request').user
		feed = Feed.objects.create(author=author, **validated_data)
		return feed