# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response

# models imports
from apps.authentication.models import UserMaster
from apps.task_mgmt.models import TaskMaster

# permissions
from rest_framework.permissions import AllowAny, IsAuthenticated

# serializers
from apps.task_mgmt.serializers import TaskMasterSerializer
from apps.base.serializers import UUIDFeildSerializer

# swager imports
from drf_spectacular.utils import extend_schema


class TaskView(APIView):
    # allowed permissions
    permission_classes = [IsAuthenticated]
    # authentication_classes = [decode_jwt_token]

    # Swagger Schema for post api
    @extend_schema(
        request=TaskMasterSerializer,
    )
    def post(self, request, *args, **kwargs):
        """method to add a new task"""
        # input data
        input_data = request.data

        # get user id from jwt token
        user_id = request.user.id

        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        user_obj = UserMaster.objects.filter(id=validated_user_id).first()
        if user_obj is None:
            return Response({"error": "Student not found"}, status=400)

        input_data["user"] = user_obj.id
        task_data_serializers = TaskMasterSerializer(data=input_data)

        # handle incomplete and invalid inputs
        if not task_data_serializers.is_valid():
            return Response({"error": task_data_serializers.errors}, status=400)

        task_data_serializers.save()

        # final_data = {"student": user_obj, **input_data}

        # # create new expense
        # task_obj = TaskMaster.objects.create(**final_data)
        return Response({"message": "Task added"}, status=201)

    def get(self, request, task_id=None, *args, **kwargs):
        """method to get all tasks or specific tasks"""
        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        user_obj = UserMaster.objects.filter(id=validated_user_id).first()
        if user_obj is None:
            return Response({"error": "User not found"}, status=400)

        # get all task
        if task_id is None:
            task_objects = TaskMaster.objects.filter(user=user_obj)
            serializer = TaskMasterSerializer(task_objects, many=True)
            return Response(serializer.data, status=200)

        # get specific task
        task_obj = TaskMaster.objects.filter(
            user=user_obj, id=task_id
        ).first()
        if task_obj is None:
            return Response({"error": "Task not found"}, status=404)

        task_serializer = TaskMasterSerializer(task_obj)
        return Response(task_serializer.data, status=200)


    def patch(self, request, task_id=None, *args, **kwargs):
        """method to update specific task"""

        if task_id is None:
            return Response({"error": "Task id is required"}, status=400)

        # serialize input data
        input_data = request.data

        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        user_obj = UserMaster.objects.filter(id=validated_user_id).first()
        if user_obj is None:
            return Response({"error": "User not found"}, status=400)

        # get specific task
        task_obj = TaskMaster.objects.filter(
            user=user_obj, id=task_id
        ).first()
        if task_obj is None:
            return Response({"error": "Task not found"}, status=404)

        task_data_serializers = TaskMasterSerializer(data=input_data)

        # handle incomplete and invalid inputs
        if not task_data_serializers.is_valid():
            return Response({"error": task_data_serializers.errors}, status=400)

        # update the expense
        task_updated_data = TaskMasterSerializer(
            task_obj, input_data, partial=True
        )

        if not task_updated_data.is_valid():
            return Response({"error": task_updated_data.errors}, status=400)

        task_updated_data.save()
        return Response({"message": "task updated"}, status=200)

    def delete(self, request, task_id=None, *args, **kwargs):
        """method to delete specific tasks"""

        if task_id is None:
            return Response({"error": "Task id is required"}, status=400)

        # get user id from jwt token
        user_id = request.user.id

        # check uuid
        user_id_serializer = UUIDFeildSerializer(data={"id": user_id})
        if not user_id_serializer.is_valid():
            return Response({"error": user_id_serializer.errors}, status=400)

        validated_user_id = user_id_serializer.validated_data.get("id")

        # check the user exists
        user_obj = UserMaster.objects.filter(id=validated_user_id).first()
        if user_obj is None:
            return Response({"error": "User not found"}, status=400)

        # get specific task
        task_obj = TaskMaster.objects.filter(
            user=user_obj, id=task_id
        ).first()
        if task_obj is None:
            return Response({"error": "Task not found"}, status=404)

        task_obj.delete()
        return Response({"message": "Task deleted"}, status=200)
