from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, RoomCategory
from .forms import RoomForm, RoomCategoryForm




# Index view
def index(request):
    categories = RoomCategory.objects.all()  # Fetch all categories
    return render(request, 'index.html', {'categories': categories})

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
                return redirect('adminpannel')
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



# Admin panel view with property form
def admin_panel(request):
    return render(request, 'adminPannel.html')



# Room Category Views
def room_category_list(request):
    categories = RoomCategory.objects.all()
    return render(request, 'room_category_list.html', {'categories': categories})



from django.shortcuts import render, redirect
from .forms import RoomCategoryForm

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
from django.shortcuts import get_object_or_404, redirect
from .models import RoomCategory

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



