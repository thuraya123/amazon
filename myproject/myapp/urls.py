from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('customer_profile/', views.customer_profile, name='customer_profile'),
    path('organization_profile/', views.organization_profile, name='organization_profile'),

    # Add other URL patterns as needed
]
