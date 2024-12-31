from django import forms
from .models import RoomCategory, Room, Testimonial


class RoomCategoryForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = ['name', 'image', 'description']  # Add description field to the form

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['category', 'image']  # Only category and image fields




class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'image', 'review', 'rating']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your review here...'}),
            'rating': forms.Select(),
        }


# forms.py
from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender_email = forms.EmailField()



from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 4px;',
                'placeholder': 'Your Name'
            }
        )
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 4px;',
                'placeholder': 'Your Email'
            }
        )
    )
    
    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px w #ddd; border-radius: 4px;',
                'placeholder': 'Subject'
            }
        )
    )
    
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'style': 'width: 100%; padding: 8px; margin-bottom: 15px; border: 1px solid #ddd; border-radius: 4px; min-height: 150px;',
                'placeholder': 'Your Message',
                'rows': 6
            }
        )
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']