# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
# from activity.models import UserActivity
# from activity.api.serializers import UserActivitySerializer

# # List all user activities
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def user_activity_list(request):
#     activities = UserActivity.objects.all()
#     serializer = UserActivitySerializer(activities, many=True)
#     return Response(serializer.data)

# # # Get the first user activity record
# # @api_view(['GET'])
# # def user_activity_first(request):
# #     activity = UserActivity.objects.first()
# #     if not activity:
# #         return Response({"detail": "No activity found."}, status=status.HTTP_404_NOT_FOUND)
# #     serializer = UserActivitySerializer(activity)
# #     return Response(serializer.data, status=status.HTTP_200_OK)

# # Add a new user activity
# @api_view(['POST'])
# def user_activity_add(request):
#     activity_data = request.data
#     serializer = UserActivitySerializer(data=activity_data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# # Update an existing user activity
# @api_view(['POST'])
# def user_activity_update(request, id):
#     activity = UserActivity.objects.filter(id=id).first()
#     if not activity:
#         return Response({"detail": "Activity not found."}, status=status.HTTP_404_NOT_FOUND)
    
#     activity_data = request.data
#     serializer = UserActivitySerializer(data=activity_data, instance=activity)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

# # Delete a user activity
# @api_view(['POST'])
# def user_activity_delete(request, id):
#     activity = UserActivity.objects.filter(id=id).first()
#     if not activity:
#         return Response({"detail": "Activity not found."}, status=status.HTTP_404_NOT_FOUND)
    
#     activity.delete()
#     return Response({
#         "message": "Activity deleted successfully."
#     }, status=status.HTTP_204_NO_CONTENT)
