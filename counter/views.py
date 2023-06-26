from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the dashboard or any other page
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})


def welcome(request):
    return render(request, 'home.html')
    

def home(request):
    return render(request, 'landingpage.html')