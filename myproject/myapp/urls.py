from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('customer/signup/', views.customer_signup, name='customer_signup'),
    path('organization/signup/', views.organization_signup, name='organization_signup'),
    path('customer/login/', views.customer_login, name='customer_login'),
    path('organization/login/', views.organization_login, name='organization_login'),
    path('home/', views.home, name='home'),
    path('shopping_list/', views.shopping_list, name='shopping_list'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('customer/home/', views.customer_homepage, name='customer_homepage'),
    path('organization/home/', views.organization_homepage, name='organization_homepage'),
    path('pick1/', views.signup_choice, name='signup_choice'),
    path('customer/profile/', views.customer_profile, name='customer_profile'),
    path('organization/profile/', views.organization_profile, name='organization_profile'),
    path('', views.main_page, name='mainpage'),
    path('pick2/', views.login_choice, name='login_choice'), 
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('delivery/', views.delivery, name='delivery_form'),
    path('organization/<int:organization_id>/delivery-requests/', views.organization_delivery_requests, name='organization_delivery_requests'),
    

    # Add other URL patterns as needed
]
