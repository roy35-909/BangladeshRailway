from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your views here.
class User(AbstractUser):
    phone = models.CharField(max_length=50, unique=True)
    otp = models.CharField(max_length=50,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password_forget_token = models.CharField(max_length=300,null=True,blank=True)
    REQUIRED_FIELDS = ['password']
