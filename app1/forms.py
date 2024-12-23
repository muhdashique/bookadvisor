from django import forms
from .models import RoomCategory, Room


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'image', 'description']  # Add description field to the form

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'image']  # Only category and image fields




from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'background_image', 'review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
            'rating': forms.Select(),
        }



