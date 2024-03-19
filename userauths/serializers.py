from rest_framework import serializers

from userauths.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user).data
        return response
