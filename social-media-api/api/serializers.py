from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}} # password only for write.
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)