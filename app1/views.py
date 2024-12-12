from django.shortcuts import render # type: ignore
from django.contrib.auth import authenticate, login# type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.contrib.auth.forms import AuthenticationForm# type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.http import HttpResponse# type: ignore
from django.shortcuts import render, redirect # type: ignore
from .forms import RoomCategoryForm
from django.contrib import messages # type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.contrib.auth.decorators import login_required# type: ignore
from django.contrib import messages# type: ignore

# Create your views here.

# home page views
def Index(request):
    return render(request,"index.html")


# about page views
def About(request):
    return render(request,"about.html")


# property page views
def property_list(request):
    return render(request, 'property.html')

# contact page views
def contact(request):
    return render(request, 'contact.html')


# login page views
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('adminpannel')  # Corrected to match the URL pattern
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


# adminpannel page view
def AdminPannel(request):
    return render(request, 'adminPannel.html')

# admin pannel view
def AdminPannel(request):
    if request.method == "POST":
        form = RoomCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Room Category added successfully!")
            return redirect('adminpannel')  # Redirect to reload the page
    else:
        form = RoomCategoryForm()

    return render(request, 'adminpannel.html', {'form': form})


# propertyview page view
def PropertyView(request):
    return render(request,'propertyView.html') 









