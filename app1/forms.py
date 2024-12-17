from django import forms
from .models import RoomCategory, Room


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'description', 'image']

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'name', 'description', 'price', 'image', 'is_available']




