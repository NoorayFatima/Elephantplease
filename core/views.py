from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def rent(request):
    return render(request, 'core/rent.html')

def lend(request):
    return render(request, 'core/lend.html')

def search(request):
    return render(request, 'core/search.html')

def sign_in(request):
    return render(request, 'core/sign in.html')
    