from django.views.generic import TemplateView

from properties.models import Property

class HomePageView(TemplateView):
	  template_name = 'index.html'

	  def get_context_data(self, *args, **kwargs):
	  	context = super(HomePageView, self).get_context_data(*args, **kwargs)

	  	properties = Property.objects.all()

	  	context['number_of_properties'] = len(properties)

	  	return context
