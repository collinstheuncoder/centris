from django.contrib import admin

from .models import Location
from .forms import LocationAddForm

# Register your models here.
class LocationAdmin(admin.ModelAdmin):
    model = Location
    form = LocationAddForm

admin.site.register(Location, LocationAdmin)
 
