from django.contrib import admin

from .forms import PropertyCreateForm
from .models import Property

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
		form = PropertyCreateForm
		list_display = ('property_id', 'property_type', 'location', 'is_for_sale', 'cost', 'num_of_bedrooms', 'num_of_bathrooms', 'has_pool', 'has_waterfront')
