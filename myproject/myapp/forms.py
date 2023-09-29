# accounts/forms.py
from django import forms
from .models import ShoppingListItem

from django import forms
from .models import ShoppingListItem

class ShoppingListItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingListItem
        fields = ['product_name', 'product_type', 'expiration_date', 'quantity', 'amount_of_food']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }


from django import forms

from django import forms

class CustomerSignupForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    reconfirm_password = forms.CharField(widget=forms.PasswordInput, label="Reconfirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        reconfirm_password = cleaned_data.get("reconfirm_password")

        if password != reconfirm_password:
            raise forms.ValidationError("Passwords do not match.")

class OrganizationSignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    industry = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    reconfirm_password = forms.CharField(widget=forms.PasswordInput, label="Reconfirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        reconfirm_password = cleaned_data.get("reconfirm_password")

        if password != reconfirm_password:
            raise forms.ValidationError("Passwords do not match.")

from django import forms

class CustomerLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

class OrganizationLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py

from django import forms
from .models import Customer, Organization

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['profile_picture', 'pickup_location']

class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['profile_picture', 'location', 'industry']
