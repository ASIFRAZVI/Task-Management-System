# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# models imports
from apps.authentication.models import UserMaster

# permissions
from rest_framework.permissions import AllowAny

# serializers
from apps.authentication.serializers import UserRegistrationSerializers

# password processors
from django.contrib.auth.hashers import make_password

# swager imports
from drf_spectacular.utils import extend_schema


class UserRegisteration(APIView):
    # allowed permissions
    permission_classes = [AllowAny]

    # Swagger Schema for post api
    @extend_schema(
        request=UserRegistrationSerializers,
    )
    def post(self, request, *args, **kwargs):
        """method to register user"""
        # serialize input data
        input_data = request.data
        user_data_serializers = UserRegistrationSerializers(data=input_data)

        # handle incomplete and invalid inputs
        if not user_data_serializers.is_valid():
            return Response({"error": user_data_serializers.errors}, status=400)

        # prepocessing
        input_email = input_data.get("email", None)
        password = input_data.get("password")

        # check the uniqueness of email
        user_obj = UserMaster.objects.filter(email=input_email).first()
        if user_obj is not None:
            return Response({"error": "entered email already exists!"}, status=400)

        # update the email in serializers data
        input_data["email"] = input_email

        # hashed_password
        hashed_password = make_password(password)

        # hash the password
        final_data = {**input_data, "password": hashed_password}

        # save the data
        user_data = UserRegistrationSerializers(data=final_data)

        if not user_data.is_valid():
            return Response({"error": user_data.errors}, status=400)
        user_data.save()

        return Response({"message": "ohoo! user registered"}, status=201)
