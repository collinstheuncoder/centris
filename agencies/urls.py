from django.urls import path
from . import views

urlpatterns = [
		path('', views.AgencyListView.as_view(), name='agency_list'),
		path('<str:id>/', views.AgencyDetailView.as_view(), name='agency_detail'),
]
