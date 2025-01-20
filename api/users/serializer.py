from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email', 'username', 'created_at')
		read_only_fields = ('created_at',)

class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
	password2 = serializers.CharField(write_only=True, required=True)

	class Meta:
		model = User
		fields = ('email', 'username', 'password', 'password2')

	def validate(self, attrs):
		if attrs['password'] != attrs['password2']:
			raise serializers.ValidationError({"password": "Password fields didn't match."})
		return attrs

	def create(self, validated_data):
		validated_data.pop('password2')
		user = User.objects.create_user(**validated_data)
		return user

class LoginSerializer(serializers.Serializer):
	email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True)

	def validate(self, attrs):
		user = authenticate(username=attrs['email'], password=attrs['password'])
		if not user:
			raise serializers.ValidationError('Invalid email or password.')
		attrs['user'] = user
		return attrs