# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# models imports
from apps.authentication.models import UserMaster

# permissions
from rest_framework.permissions import AllowAny


# serializers
from apps.authentication.serializers import UserLoginSerializers

# password processors
from django.contrib.auth.hashers import check_password

# swager imports
from drf_spectacular.utils import extend_schema

# jwt processors
# from apps.helpers.jwt_generator import generate_jwt_token, generate_refresh_token
from rest_framework_simplejwt.tokens import RefreshToken

# settings
from django.conf import settings


class UserLoginView(APIView):
    # allowed permissions
    # permission_classes = [AllowAny]
    # authentication_classes = []

    # Swagger Schema for post api
    @extend_schema(
        request=UserLoginSerializers,
    )
    def post(self, request, *args, **kwargs):
        """method to login user and store the cookies"""
        input_data = request.data

        # serializ the input data
        login_serializer = UserLoginSerializers(data=input_data)
        if not login_serializer.is_valid():
            return Response({"error": login_serializer.errors}, status=400)

        validated_email = login_serializer.validated_data.get("email")
        validated_password = login_serializer.validated_data.get("password")

        user_obj = UserMaster.objects.filter(email=validated_email).first()

        if user_obj is None:
            return Response(
                {"error": "Entered user email doesn't registered!"}, status=400
            )

        if user_obj.is_active is False:
            return Response(
                {
                    "error": "Account is deactivated!, please do activate the account by email otp!"
                },
                status=400,
            )

        if check_password(validated_password, user_obj.password):
            refresh = RefreshToken.for_user(user_obj)

            response = Response(
                {
                    "acess_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "ok": "cookies stored!",
                },
                status=200,
            )

            # Set token in cookies
            response.set_cookie("access_token", str(refresh.access_token), httponly=True)
            response.set_cookie("refresh_token", str(refresh), httponly=True)

            return response

        return Response({"error": "invalid password"}, status=400)
