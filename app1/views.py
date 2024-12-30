from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomCategory
from .forms import RoomForm, RoomCategoryForm
from django.shortcuts import render
from .forms import TestimonialForm
from .models import Testimonial, RoomCategory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




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

    return render(request, 'adminpannel.html', {'form': form, 'testimonials': testimonials, 'categories': categories})




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
