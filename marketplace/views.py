from django.shortcuts import render

def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    return render(request, 'marketplace/listings.html')