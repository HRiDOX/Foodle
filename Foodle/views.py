from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def home_vendor(request):
    return render(request, 'home_vendor.html')    