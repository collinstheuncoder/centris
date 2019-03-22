from django.contrib import admin

from .forms import AgencyForm
from .models import Agency

# Register your models here.
@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
		list_display = ('agency_id', 'name', 'location')
		form = AgencyForm
