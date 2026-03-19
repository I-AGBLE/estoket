from django.shortcuts import render
from .forms import LoginForm, SignupForm

# Create your views here.
def index(request):
    form = LoginForm
    return render(request, 'index.html', {'form': form})

def signup(request):
    form = SignupForm
    return render(request, 'signup.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')
