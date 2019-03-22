from django import forms
from .models import Property

class PropertyCreateForm(forms.ModelForm):
		class Meta:
				model = Property
				fields = [
						'property_type', 
						'is_for_sale', 
						'cost', 
						'location', 
						'num_of_bedrooms', 
						'num_of_bathrooms', 
						'num_of_parking_spaces', 
						'num_of_garages',
						'has_pool',
						'has_waterfront',
						'has_elevator',
						'added_on',
				]
