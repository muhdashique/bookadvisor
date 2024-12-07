from django.shortcuts import render # type: ignore
from django.contrib.auth import authenticate, login# type: ignore
from django.shortcuts import render, redirect# type: ignore
from django.contrib.auth.forms import AuthenticationForm# type: ignore

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
                return redirect('home')  # Redirect to homepage or another view
            else:
                form.add_error(None, "Invalid credentials")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})