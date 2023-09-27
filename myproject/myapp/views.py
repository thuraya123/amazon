from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm  # Import the registration and login forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Handle user registration logic here
            return redirect('home')  # Redirect to the home page after registration
        else:
            # Check for password validation errors
            if 'password1' in form.errors:
                messages.error(request, 'Password is not valid. Please choose a stronger password.')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Set the category in the session or as needed
            if user.category == 'customer':
                request.session['category'] = 'customer'
                return redirect('home')  # Redirect to the customer home page
            elif user.category == 'organization':
                request.session['category'] = 'organization'
                return redirect('home')  # Redirect to the organization home page
        else:
            # Display an error message for invalid login credentials
            messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    # Your view logic here
    return render(request, 'home.html')
# views.py

from django.shortcuts import render, redirect
from .models import CustomerProfile, OrganizationProfile
from .forms import CustomerProfileForm, OrganizationProfileForm
@login_required
def customer_profile(request):
    user = request.user  # Get the authenticated user
    profile = CustomerProfile.objects.get(user=user)
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = CustomerProfileForm(instance=profile)
    return render(request, 'customer_profile.html', {'profile': profile, 'form': form, 'user': user})

@login_required
def organization_profile(request):
    user = request.user  # Get the authenticated user
    profile = OrganizationProfile.objects.get(user=user)
    if request.method == 'POST':
        form = OrganizationProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
    else:
        form = OrganizationProfileForm(instance=profile)
    return render(request, 'organization_profile.html', {'profile': profile, 'form': form, 'user': user})
