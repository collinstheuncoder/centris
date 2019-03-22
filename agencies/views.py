from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Agency

# Create your views here.
class AgencyListView(ListView):
		model = Agency
		template_name = 'agency_list.html'

class AgencyDetailView(DetailView):
		model = Agency
		template_name = 'agency_detail.html'

class AgencyCreateView(LoginRequiredMixin, CreateView):
		model = Agency
		template_name = 'agency_new.html'
		fields = ['name', 'location',]
		login_url = 'login'

		def form_valid(self, form):
				form.instance.author = self.request.user
				return super().form_valid(form)

class AgencyUpdateView(LoginRequiredMixin, UpdateView):
		model = Agency
		fields = ['name', 'location', ]
		template_name = 'agency_edit.html'
		login_url = 'login'

		def form_valid(self, form):
				form.instance.author = self.request.user
				return super().form_valid(form)

class AgencyDeleteView(LoginRequiredMixin, DeleteView):
		model = Agency
		template_name = 'agency_delete.html'
		success_url = reverse_lazy('agency_list')
		login_url = 'login'
