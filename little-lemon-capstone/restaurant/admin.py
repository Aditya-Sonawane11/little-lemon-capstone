from django.contrib import admin
from .models import MenuItem, Booking

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "inventory")
    search_fields = ("title", "category")

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "no_of_guests", "booking_date", "user")
    list_filter = ("booking_date",)
