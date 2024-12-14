from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('properties/', views.property_list, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('adminpannel/', views.admin_pannel, name='adminpannel'),
    path('property-view/', views.PropertyView, name='property_view'),
]