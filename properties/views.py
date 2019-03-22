from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Property

# Create your views here.
class PropertyListView(ListView):
		model = Property
		template_name = 'property_list.html'

class PropertyDetailView(DetailView):
		model = Property
		template_name = 'property_detail.html'

class PropertyCreateView(LoginRequiredMixin, CreateView):
		model = Property
		template_name = 'property_new.html'
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

		login_url = 'login'

		def form_valid(self, form):
				form.instance.author = self.request.user
				return super().form_valid(form)

class PropertyUpdateView(LoginRequiredMixin, UpdateView):
		model = Property
		fields = ['title', 'body', ]
		template_name = 'property_edit.html'
		login_url = 'login'

class PropertyDeleteView(LoginRequiredMixin, DeleteView):
		model = Property
		template_name = 'property_delete.html'
		success_url = reverse_lazy('property_list')
		login_url = 'login'
