from rest_framework import serializers
from activity.models import UserActivity

class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActivity
        fields = ['id', 'user', 'user_agent', 'ip_address', 'location', 'created_time']
        