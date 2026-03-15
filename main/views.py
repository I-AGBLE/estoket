from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'public/index.html')

def all_services(request):
    return render(request, 'services/index.html')

def service(request):
    return render(request, 'services/service.html')