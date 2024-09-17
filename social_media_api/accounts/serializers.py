from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    # Use serializers.CharField for the password field and set it to write-only
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Create a new user using get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email'),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture')
        )
        # Create a token for the newly created user
        Token.objects.create(user=user)

        return user
