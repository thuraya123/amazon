# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    pickup_location = models.CharField(max_length=120, blank=True, null=True)
    # Add additional fields specific to customers here (e.g., profile picture, address, etc.)

from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Remove the organization_name field
    industry = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)


    # Add other fields specific to organizations as needed

    def __str__(self):
        return self.user.username  # You can return the organization's username or any other identifier

# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

class ShoppingListItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=100)
    expiration_date = models.DateField(null=True, blank=True)
    quantity = models.PositiveIntegerField()
    amount_of_food = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name
