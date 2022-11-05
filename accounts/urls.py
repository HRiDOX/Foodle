from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.myVendorAccount),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),

    path('login/', views.login, name='login'),
    path('login_vendor/', views.login_vendor, name='login_vendor'),
    path('logout/', views.logout, name='logout'),
    path('myUserAccount/',views.myUserAccount, name='myUserAccount'),
    path('myVendorAccount/',views.myVendorAccount, name='myVendorAccount'),
    path('custDashboard/', views.custDashboard, name='custDashboard'),
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),
    path('activateUser/<uidb64>/<token>/', views.activateUser, name='activateUser'),
    path('activateVendor/<uidb64>/<token>/', views.activateVendor, name='activateVendor'),


    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/', views.reset_password_validate, name='reset_password_validate'),
    path('reset_password/', views.reset_password, name='reset_password'),

    path('vendor/', include('vendor.urls')),
    path('customer/', include('customers.urls')),



]
