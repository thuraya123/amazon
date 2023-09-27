from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_organization = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    
    # Add any additional fields you want for your user model here
    
    def __str__(self):
        return self.username

# models.py

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)
    # Add fields specific to customer profile

class OrganizationProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    company_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    # Add fields specific to organization profile
