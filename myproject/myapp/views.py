# accounts/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import DeliveryRequest, Organization, ShoppingListItem
from .forms import CustomerLoginForm, DeliveryForm, OrganizationLoginForm, ShoppingListItemForm
#from .models import Customer, Organization  # Import the Organization model

from django.shortcuts import render, redirect
from django.contrib.auth.models import User  # Import User model if needed
from .models import Customer  # Import the Customer model

# Your other imports and view functions

from django.shortcuts import render, redirect

from .forms import CustomerSignupForm, OrganizationSignupForm

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer

from .forms import CustomerSignupForm
from django.contrib.auth.models import User
from .models import Customer  # Import your Customer model

from django.contrib.auth.models import User

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            # Check if the username is already taken
            if User.objects.filter(username=username).exists():
                # Handle the case where the username is not available
                # You can display an error message or redirect back to the signup page
                return HttpResponse("Username already taken, please choose another.")
            
            # The username is available, create the new user
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            # Continue with the rest of your signup logic


            # Create a Customer object associated with the user
            customer = Customer(user=user)
            customer.save()

            # Redirect to a success page or another view
            return redirect('customer_login')  # Replace 'success_signup' with your desired URL name
    else:
        # If it's a GET request, create a new empty form
        form = CustomerSignupForm()

    # Render the template with the form
    return render(request, 'customer_signup.html', {'form': form})


def organization_signup(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = OrganizationSignupForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Extract form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            industry = form.cleaned_data['industry']

            # Create a new User object
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            # Create an Organization object associated with the user
            organization = Organization(user=user,  industry=industry)
            organization.save()

            # Redirect to a success page or another view
            return redirect('organization_login')  # Replace 'organization_login' with your desired URL name
    else:
        # If it's a GET request, create a new empty form
        form = OrganizationSignupForm()

    # Render the template with the form
    return render(request, 'organization_signup.html', {'form': form})



from django.shortcuts import render, redirect
from .models import ShoppingListItem
from .forms import ShoppingListItemForm

def shopping_list(request):
    if request.user.is_authenticated:
        shopping_items = ShoppingListItem.objects.filter(customer=request.user)
        return render(request, 'shopping_list.html', {'shopping_items': shopping_items})
    else:
        return redirect('login')  # Redirect to the login page if the user is not logged in


def add_item(request):
    if request.method == 'POST':
        form = ShoppingListItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.customer = request.user
            item.save()
            return redirect('shopping_list')
    else:
        form = ShoppingListItemForm()
    return render(request, 'add_item.html', {'form': form})

def edit_item(request, item_id):
    item = ShoppingListItem.objects.get(id=item_id, customer=request.user)
    if request.method == 'POST':
        form = ShoppingListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shopping_list')
    else:
        form = ShoppingListItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = ShoppingListItem.objects.get(id=item_id, customer=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('shopping_list')
    return render(request, 'delete_item.html', {'item': item})

def home(request):
    # Your view logic here
    return render(request, 'home.html')

from django.contrib.auth import authenticate, login

def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to the customer dashboard or another page
                return redirect('customer_homepage')
    else:
        form = CustomerLoginForm()
    return render(request, 'customer_login.html', {'form': form})

def organization_login(request):
    if request.method == 'POST':
        form = OrganizationLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirect to the organization dashboard or another page
                return redirect('organization_homepage')
    else:
        form = OrganizationLoginForm()
    return render(request, 'organization_login.html', {'form': form})
from django.shortcuts import render

def customer_homepage(request):
    return render(request, 'customer_homepage.html', {'user': request.user})

def organization_homepage(request):
    return render(request, 'organization_homepage.html', {'user': request.user})
def signup_choice(request):
    return render(request, 'signup_choice.html')

# views.py

from django.shortcuts import render, redirect
from .models import Customer, Organization
from .forms import CustomerProfileForm, OrganizationProfileForm

def customer_profile(request):
    customer = Customer.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = CustomerProfileForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_profile')
    else:
        form = CustomerProfileForm(instance=customer)

    return render(request, 'customer_profile.html', {'form': form})

def organization_profile(request):
    organization = Organization.objects.get(user=request.user)
    
    if request.method == 'POST':
        form = OrganizationProfileForm(request.POST, request.FILES, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_profile')
    else:
        form = OrganizationProfileForm(instance=organization)

    return render(request, 'organization_profile.html', {'form': form})
from django.contrib.auth.decorators import login_required

def main_page(request):
    # Add any necessary context data here
    return render(request, 'mainpage.html')

from django.shortcuts import render

def login_choice(request):
    return render(request, 'login_choice.html')

def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            shopping_list_item = form.cleaned_data['shopping_list_item']
            organization = form.cleaned_data['organization']
            location = form.cleaned_data['location']
            delivery_datetime = form.cleaned_data['delivery_datetime']

            # Create a new DeliveryRequest object and save it to the database.
            delivery_request = DeliveryRequest(
                customer=request.user,
                shopping_list_item=shopping_list_item,
                organization=organization,
                location=location,
                delivery_datetime=delivery_datetime
            )
            delivery_request.save()

            # Redirect to a success page or homepage.
            return redirect('customer_homepage')

    else:
        form = DeliveryForm()

    return render(request, 'delivery_form.html', {'form': form})
def organization_delivery_requests(request, organization_id):
    organization = Organization.objects.get(id=organization_id)
    delivery_requests = DeliveryRequest.objects.filter(organization=organization)

    # Now, you can use 'delivery_requests' in your template to display the data.
    return render(request, 'organization_delivery_requests.html', {'delivery_requests': delivery_requests})
def organization_homepage(request):
    # Assuming the organization is associated with the logged-in user
    organization = Organization.objects.get(user=request.user)

    return render(request, 'organization_homepage.html', {'organization': organization})
