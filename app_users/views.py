from django.shortcuts import render
from .forms import LoginForm, SignupForm, CompanyForm

# Create your views here.
def index(request):
    form = LoginForm
    return render(request, 'index.html', {'form': form})

def signup(request):
    sign_up_form = SignupForm()
    login_form = LoginForm()
    
    return render(request, 'signup.html', {
        'sign_up_form': sign_up_form,
        'login_form': login_form
        })

def profile(request):
    return render(request, 'profile.html')

def signup_continue(request):
    signup_form = SignupForm()
    
    return render(request, 'signup_continue.html', {
        'signup_form': signup_form
    })
    
def register_company(request):
    register_company_form = CompanyForm()
    
    return render(request, 'company/register_company.html', {
        'register_company_form': register_company_form
    })
