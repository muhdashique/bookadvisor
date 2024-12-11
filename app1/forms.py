
from django import forms # type: ignore
from .models import RoomCategory

class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'description']
