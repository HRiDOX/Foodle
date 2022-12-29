from django.contrib import admin
from vendor.models import Vendor,OpeningHour,Seat

class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'vendor_name')
    list_editable = ('is_approved',)

class OpeningHourAdmin(admin.ModelAdmin):
    list_display = ('vendor','day','from_hour','to_hour')

class SeatAdmin(admin.ModelAdmin):
    list_display = ('vendor','total_seats','avaiable_seats')



admin.site.register(Vendor, VendorAdmin)
admin.site.register(OpeningHour,OpeningHourAdmin)
admin.site.register(Seat,SeatAdmin)