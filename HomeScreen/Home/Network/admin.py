from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
from .models import Customer, Bookmark, CustomerBookmark

#admin.site.register(Customer)
admin.site.register(Bookmark)
admin.site.register(CustomerBookmark)

@admin.register(Customer)
class CustomerAdmin(OSMGeoAdmin):
    default_lon = 1400000
    default_lat = 7495000
    default_zoom = 12