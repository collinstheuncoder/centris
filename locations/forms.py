from django import forms
from .models import Location

class LocationAddForm(forms.ModelForm):
		class Meta:
				model = Location
				fields = ['city']
