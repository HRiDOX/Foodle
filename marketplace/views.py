from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

#from accounts.models import UserProfile
#from .context_processors import get_cart_counter, get_cart_amounts
from menu.models import Category, FoodItem

from vendor.models import Vendor
from django.db.models import Prefetch
from .models import Cart
#from django.contrib.auth.decorators import login_required
#from django.db.models import Q
#
#from django.contrib.gis.geos import GEOSGeometry
#from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
#from django.contrib.gis.db.models.functions import Distance
#
#from datetime import date, datetime
#from orders.forms import OrderForm


def marketplace(request):
    vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)
    vendor_count = vendors.count()
    context = {
        'vendors': vendors,
        'vendor_count': vendor_count,
    }
    return render(request, 'marketplace/listings.html', context)


def vendor_detail(request, vendor_slug):
    vendor = get_object_or_404(Vendor, vendor_slug=vendor_slug)
#
    categories = Category.objects.filter(vendor=vendor).prefetch_related(
        Prefetch(
            'fooditems',
            queryset = FoodItem.objects.filter(is_available=True)
        )
    )
#
    #opening_hours = OpeningHour.objects.filter(vendor=vendor).order_by('day', 'from_hour')
    #
    ## Check current day's opening hours.
    #today_date = date.today()
    #today = today_date.isoweekday()
    #
    #current_opening_hours = OpeningHour.objects.filter(vendor=vendor, day=today)
    #if request.user.is_authenticated:
    #    cart_items = Cart.objects.filter(user=request.user)
    #else:
    #    cart_items = None
    context = {
        'vendor': vendor,
        'categories': categories,
    #    'cart_items': cart_items,
    #    'opening_hours': opening_hours,
    #    'current_opening_hours': current_opening_hours,
    }
    return render(request, 'marketplace/vendor_detail.html', context)


def add_to_cart(request, food_id):
    if request.user.is_authenticated:
        pass
