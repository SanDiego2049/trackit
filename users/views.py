from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from .admin import UserCreationForm
from .forms import LoginForm



def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

              
def logout(request):
       logout(request)
       return redirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)    
                return redirect('/')
        else:
            form = LoginForm()
    
    return render(request, 'login.html',{'form':form})