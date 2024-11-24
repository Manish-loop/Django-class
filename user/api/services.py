from activity.models import UserActivity

class UserServices():
    def create_user_activity(self, **kwargs):
        data = UserActivity.objects.create(
            user = kwargs.get('user'),
            user_agent = kwargs.get('user_agent'),
            ip_address = kwargs.get('ip_address'),
            location = kwargs.get('location'),
            modules = kwargs.get('modules')
        )
        return True