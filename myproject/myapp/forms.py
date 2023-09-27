from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class RegistrationForm(UserCreationForm):
    category_choices = (
        ('customer', 'Customer'),
        ('organization', 'Organization'),
    )
    
    category = forms.ChoiceField(
        choices=category_choices,
        required=True,
        widget=forms.RadioSelect(attrs={'class': 'category-radio'}),
    )

    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ('username', 'email', 'password1', 'password2', 'category')

from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    category = forms.CharField(widget=forms.HiddenInput())  # Add a hidden field for category
    
    class Meta:
        fields = ('username', 'password')

# forms.py

from django import forms
from .models import CustomerProfile, OrganizationProfile

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = CustomerProfile
        fields = ['profile_picture', 'location']  # Add other fields here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(max_length=150, initial=self.instance.user.username, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        self.fields['email'] = forms.EmailField(initial=self.instance.user.email, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))

class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model = OrganizationProfile
        fields = ['profile_picture', 'location']  # Add other fields here

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = forms.CharField(max_length=150, initial=self.instance.user.username, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
        self.fields['email'] = forms.EmailField(initial=self.instance.user.email, widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
