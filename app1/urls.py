from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('properties/', views.property_list, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('admin-panel/', views.admin_pannel, name='admin_pannel'),
    path('categories/', views.room_category_list, name='room_category_list'),
    path('categories/add/', views.add_room_category, name='add_room_category'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/<int:category_id>/', views.room_list, name='room_list_by_category'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('categories/edit/<int:category_id>/', views.edit_room_category, name='edit_room_category'),
    path('categories/delete/<int:category_id>/', views.delete_room_category, name='delete_room_category'),
    path('room-category/<int:category_id>/', views.room_category_detail, name='room_category_list'),
    path('property/view/<int:category_id>/', views.property_view, name='property_view'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('room/<int:id>/', views.room_view, name='room_view'),
    path('add-images-to-room/<int:room_id>/', views.add_images_to_room, name='add_images_to_room'),
    path('room/<int:id>/', views.room_view, name='room_detail'),
    path('property/view/<int:category_id>/', views.property_view, name='property_view'),
    path('room/<int:room_id>/', views.room_view, name='room_view'),
    path('testimonials/', views.testimonial_view, name='testimonial_view'),
    path('add_testimonial/<int:id>/', views.add_testimonial, name='add_testimonial'),
    path('testimonials/', views.testimonial_list, name='testimonials'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),

     path('testimonials/', views.testimonial_list, name='testimonial_list'),
    path('testimonials/add/', views.add_edit_testimonial, name='add_testimonial'),
    path('testimonials/edit/<int:pk>/', views.add_edit_testimonial, name='edit_testimonial'),
    path('testimonials/delete/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),





   
]
     
