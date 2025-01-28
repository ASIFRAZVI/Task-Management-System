from rest_framework import serializers
from apps.authentication.models import UserMaster, OtpMaster


class UserRegistrationSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        exclude = ["id", "is_active", "last_login"]


class UserLoginSerializers(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)


class OtpSerializers(serializers.Serializer):
    otp = serializers.IntegerField()
    email = serializers.EmailField()
