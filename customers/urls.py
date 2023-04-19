from django.urls import path
from . import views
from .views import CustomerListView

   

urlpatterns=[
    path('',CustomerListView.as_view(), name='index'),
    path('add/',views.create_customer, name='add'),
    path('customer/<uuid:id>/edit/', views.edit_customer, name='edit_customers'),
    path('search/',views.search, name='search'),
    path('customer/<uuid:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('page_size/<int:page_size>/', CustomerListView.as_view(), name='index'),
]
