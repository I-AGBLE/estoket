from django.shortcuts import render
from app_users.forms import LoginForm, CompanyForm
from main.forms import ServiceForm

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
    
def dashboard(request):
    return render(request, 'company_dashboard/index.html')

def company_services(request):
    return render(request, 'company_dashboard/company_services.html')

def company_expertise(request):
    return render(request, 'company_dashboard/company_expertise.html')

def company_links(request):
    return render(request, 'company_dashboard/company_links.html')

def edit_bio(request):
    edit_company_form = CompanyForm()
    
    return render(request, 'company_dashboard/edit_bio.html', {
        'edit_company_form': edit_company_form
    })
    
    
def service_form(request):
    service_form = ServiceForm()
    
    return render(request, 'company_dashboard/add_service.html', {
        'service_form': service_form
    })