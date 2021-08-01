from rest_framework import serializers

from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )


class EmailConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()


class TokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    user_code = serializers.CharField()
