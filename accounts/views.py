from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import message
from django.shortcuts import render,HttpResponse,redirect
from .forms import UserForm
from .models import User,UserProfile
from django.contrib import messages,auth
from vendor.forms import VendorForm
from .utils import detectUser,send_verification_email
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.exceptions import PermissionDenied
from vendor.models import Vendor

# Restricting the vendor from accesssing the customer page
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied


# Restricting the customer from accessing the vendor page
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied



# Create your views here.


def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request,'You Are Already logged in!')
        return redirect('myAccount')
    elif request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            #password = form.cleaned_data['password']
            #user = form.save(commit=False)
            #user.set_password(password)
            #user.role = User.CUSTOMER
            #user.save()
             # Create the user using create_user method
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.CUSTOMER
            user.save()

            # Send Verifcation email

            send_verification_email(request, user)
            messages.success(request,'Your accout has been registered successfully!')
            return redirect('registerUser')
        else:
             print('invalid form')
             print(form.errors)
    else:
       
        form = UserForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/registerUser.html',context)



def registerVendor(request):
    if request.user.is_authenticated:
        messages.warning(request,'You Are Already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid:
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.role = User.VENDOR
            user.save()
            vendor = v_form.save(commit=False)
            vendor.user = user
            user_profile = UserProfile.objects.get(user=user)
            vendor.user_profile = user_profile
            vendor.save()
            
            # Send Verifcation email

            send_verification_email(request, user)
            messages.success(request, 'Your restaurant has been registered successfully!! Please wait for further approval')
            return redirect('registerVendor')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form  = UserForm()
        v_form = VendorForm()

    context = {
        'form':form,
        'v_form':v_form
    }

    return render(request, 'accounts/registerVendor.html',context)

def activate(request, uidb64,token):
    #Activate the user by setting the is_active status to True

    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request,'Congratulations! Your account is activated.Thank You For Choosing Us')
        return redirect('myAccount')
    else:
        messages.error(request,'Invalid Activation link')
        return redirect('myAccount')

    

def login(request):
    if request.user.is_authenticated:
        messages.warning(request,'You Are Already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Your are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request,'Invalid Login Credentials')
            return redirect('login')


    return render(request, 'accounts/login.html')
def login_vendor(request):
    if request.user.is_authenticated:
        messages.warning(request,'You Are Already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Your are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request,'Invalid Login Credentials')
            return redirect('login_vendor')

    return render(request, 'accounts/login_vendor.html')

def logout(request):
    auth.logout(request)
    messages.info(request,'You are logged out.')
    return redirect('login')

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl) 

@login_required(login_url='login')
@user_passes_test(check_role_customer)
def custDashboard(request):
    return render(request,'accounts/custDashboard.html')

@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    return redirect(request,'accounts/vendorDashboard.html')