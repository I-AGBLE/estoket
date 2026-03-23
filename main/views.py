from django.shortcuts import render
from app_users.forms import LoginForm, CompanyForm
from main.forms import ServiceForm, ExpertiseForm, FAQForm, PackageForm, LinkForm

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

def add_expertise(request):
    expertise_form = ExpertiseForm()
    
    return render(request, 'company_dashboard/add_expertise.html', {
        'expertise_form': expertise_form
    })
    
def add_faq(request):
    faq_form = FAQForm()
    
    return render(request, 'company_dashboard/add_faq.html', {
        'faq_form': faq_form
    })
    
    
    

def add_package(request):
    package_form = PackageForm()
    
    return render(request, 'company_dashboard/add_package.html', {
        'package_form': package_form
    })
    


def add_link(request):
    link_form = LinkForm()
    
    return render(request, 'company_dashboard/add_link.html', {
        'link_form': link_form
    })