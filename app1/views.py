from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomCategory
from .forms import RoomForm, RoomCategoryForm
from django.shortcuts import render
from .forms import TestimonialForm,ContactForm
from .models import Testimonial, RoomCategory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .utils import send_contact_email



# Index view
def index(request):
    # Fetch all categories
    categories = RoomCategory.objects.all()
    
    # Fetch all testimonials
    testimonials = Testimonial.objects.all()
    
    # Add stars attribute to testimonials
    for testimonial in testimonials:
        testimonial.stars = ['★'] * testimonial.rating + ['☆'] * (5 - testimonial.rating)

    # Create a testimonial form
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page after saving

    return render(request, 'index.html', {'form': form, 'testimonials': testimonials, 'categories': categories})


# About view
def About(request):
    return render(request, "about.html")

# Property list view
def property_list(request):
     categories = RoomCategory.objects.all()  # Fetch all categories
     return render(request, 'property.html', {'categories': categories})

# Contact view
def contact(request):
    return render(request, 'contact.html')

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_pannel')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# Admin panel view with property form

def admin_pannel(request):
    categories = RoomCategory.objects.all()  # Fetch all categories
    testimonials = Testimonial.objects.all()  # Fetch all testimonials
    form = TestimonialForm()

    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_pannel')  # This should match the URL pattern name

    return render(request, 'app1/adminpannel.html', {'form': form, 'testimonials': testimonials, 'categories': categories})




# Room Category Views
def room_category_list(request):
    categories = RoomCategory.objects.all()
    return render(request, 'room_category_list.html', {'categories': categories})





def add_room_category(request):
    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('room_category_list')  # Redirect to the category list view
    else:
        form = RoomCategoryForm()

    return render(request, 'add_room_category.html', {'form': form})





# Room Views
def room_list(request, category_id=None):
    if category_id:
        category = get_object_or_404(RoomCategory, id=category_id)
        rooms = Room.objects.filter(category=category)
    else:
        rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            room = form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})


# delete category

def delete_room_category(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('room_category_list')
    return redirect('room_category_list')




# edit category
def edit_room_category(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)
    if request.method == 'POST':
        form = RoomCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('room_category_list')
    else:
        form = RoomCategoryForm(instance=category)
    return render(request, 'edit_room_category.html', {'form': form})

# property view page
def property_view(request, category_id):
    category = get_object_or_404(RoomCategory, id=category_id)  # Get the category
    rooms = Room.objects.filter(category=category)  # Fetch rooms for the category
    return render(request, 'propertyView.html', {'rooms': rooms, 'category': category})




# roomlist view
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

# edit room details
def edit_room(request, room_id):
   
    room = get_object_or_404(Room, id=room_id)
    
    if request.method == 'POST':
       
        form = RoomForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, f'Room "{room.name}" updated successfully.')
            return redirect('room_list')
    else:
        # Display form for editing
        form = RoomForm(instance=room)
    
    return render(request, 'edit_room.html', {
        'form': form,
        'room': room
    })
# delete room details 
def delete_room(request, room_id):
    # Retrieve the room or show 404 if not found
    room = get_object_or_404(Room, id=room_id)
    
    
    
    # Delete the room
    room.delete()
    messages.success(request, f'Room "{room.name}" has been deleted.')
    return redirect('room_list')


def room_view(request, id):
    # Get the current room
    room = get_object_or_404(Room, id=id)
    
    # Fetch next and previous rooms based on the current room ID
    next_room = Room.objects.filter(id__gt=room.id).order_by('id').first()
    previous_room = Room.objects.filter(id__lt=room.id).order_by('-id').first()

    return render(request, 'room_view.html', {
        'room': room,
        'next_room': next_room,
        'previous_room': previous_room,
    })



def add_images_to_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    # Your logic for adding images to the room
    return render(request, 'add_images_to_room.html', {'room': room})





def room_category_detail(request, category_id):
    category = RoomCategory.objects.get(id=category_id)
    return render(request, 'room_category_list.html', {'category': category})






def testimonial_view(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('testimonial_view')  # Redirect to the same page after saving
    else:
        form = TestimonialForm()

    testimonials = Testimonial.objects.all()  # Retrieve all testimonials
    return render(request, 'add_testimonial.html', {'form': form, 'testimonials': testimonials})


def add_testimonial(request):
    return render(request,'add_testimonial.html')







from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonial
from .forms import TestimonialForm

# View to list all testimonials
def testimonial_list(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials/testimonial_list.html', {'testimonials': testimonials})



# View to add/edit a testimonial
def add_edit_testimonial(request, pk=None):
    testimonial = None
    if pk:
        testimonial = get_object_or_404(Testimonial, pk=pk)
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('testimonial_list')
    else:
        form = TestimonialForm(instance=testimonial)
    
    return render(request, 'add_testimonial.html', {
        'form': form,
        'testimonial': testimonial
    })




# View to delete a testimonial
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    return redirect('testimonial_list')




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form
            contact = form.save()
            
            # Send email
            email_sent = send_contact_email(form.cleaned_data)
            
            if email_sent:
                messages.success(request, 'Your message has been sent successfully!')
            else:
                messages.warning(request, 'Your message was saved but there was an error sending the email notification.')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Get phone number
        message = request.POST.get('message')

        if not all([name, email, phone, message]):
            messages.error(request, "All fields are required.")
            return redirect('contactus')

        try:
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Message:\n{message}"
                ),
                from_email='your_email@gmail.com',  # Replace with your email
                recipient_list=['muhammedashique8281@gmail.com'],  # Replace with recipient email
                fail_silently=False,
            )
            
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contactus')
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('contact')

    return render(request, 'contactus.html')
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ContactForm

def send_contact_email(data):
    # Compose the email body manually instead of using a template
    subject = f"New Contact Form Submission from {data['name']}"
    message = (
        f"New Contact Form Submission\n\n"
        f"Name: {data['name']}\n"
        f"Email: {data['email']}\n"
        
        f"Message:\n{data['message']}\n\n"
        f"This email was sent from your website's contact form."
    )
    
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=data['email'],  # Or use a fixed email like 'your_email@gmail.com'
            recipient_list=['muhammedashique8281@gmail.com'],  # Replace with your email
            fail_silently=False,
        )
        return True
    except Exception as e:
        return False

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data (if needed)
            contact = form.save()
            
            # Send email
            email_sent = send_contact_email(form.cleaned_data)
            
            if email_sent:
                messages.success(request, 'Your message has been sent successfully!')
            else:
                messages.warning(request, 'Your message was saved but there was an error sending the email notification.')
            
            return redirect('contactpage')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})