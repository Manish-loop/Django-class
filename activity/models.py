from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_agent = models.CharField(max_length=100, null=True, blank=True)
    ip_address = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modules = models.CharField(max_length=20, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)