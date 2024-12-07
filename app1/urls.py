from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.Index, name='index'), 
    path('about/', views.About, name='about'),  
    path('properties/', views.property_list, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    
]