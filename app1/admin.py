from django.contrib import admin
from .models import RoomCategory, Property
from .forms import PropertyForm

class PropertyAdmin(admin.ModelAdmin):
    form = PropertyForm

admin.site.register(RoomCategory)
admin.site.register(Property, PropertyAdmin)
