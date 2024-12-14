from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PropertyForm

# Index view
def index(request):
    return render(request, 'index.html')

# About view
def About(request):
    return render(request, "about.html")

# Property list view
def property_list(request):
    return render(request, 'property.html')

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
@login_required
def admin_pannel(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Property added successfully!")
            return redirect('adminpannel')
    else:
        form = PropertyForm()

    return render(request, 'adminPannel.html', {'form': form})

# Property view
def PropertyView(request):
    return render(request, 'propertyView.html')
