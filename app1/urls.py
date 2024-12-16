from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.About, name='about'),
    path('properties/', views.property_list, name='properties'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('admin-panel/', views.admin_panel, name='adminpannel'),
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

      path('rooms/', views.room_list, name='room_list'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
      path('room/<int:id>/', views.room_view, name='room_view'),
    
]