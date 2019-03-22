from django.urls import path
from . import views

urlpatterns = [
		path('', views.PropertyListView.as_view(), name='property_list'),
		path('<str:id>/', views.PropertyDetailView.as_view(), name='property_detail'),
]
