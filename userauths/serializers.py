from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from django.contrib.auth.password_validation import validate_password
from userauths.models import User, Profile


class MyTokenObtainPairSerializer(TokenObtainSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['full_name'] = user.full_name
        token['username'] = user.username
        token['email'] = user.email
        try:
            token['vendor_id'] = user.vendor.id
        except:
            token['vendor_id'] = 0

        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
        password2 = serializers.CharField(write_only=True, required=True)
        model = User
        fields = ['full_name', 'email', 'phone_number', 'password', 'password2']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"Passwords": "La contraseña no es correcta"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            full_name=validated_data['full_name'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number']
        )

        email_user, mobile = user.email.split('@')
        user.set_password(validated_data['password'])

        user.set_password(validated_data['password'])
        user.save()
        return user


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
