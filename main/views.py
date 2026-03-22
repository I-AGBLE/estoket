from django.shortcuts import render
from app_users.forms import LoginForm

# Create your views here.
def index(request):
    login_form = LoginForm()

    return render(request, 'public/index.html', {
        'login_form': login_form
    })

def all_services(request):
    return render(request, 'services/index.html')

def service(request):
    login_form = LoginForm()

    return render(request, 'services/service.html', {
        'login_form': login_form
    })

def more_services(request):
    login_form = LoginForm()

    return render(request, 'services/more_services.html', {
        'login_form': login_form
    })