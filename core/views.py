from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
#SignInForm, ForgetPasswordForm, ResetPasswordForm, ChangePasswordForm


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

def sign_up(request):
    return render(request, 'core/sign up.html')

def forget_password(request):
    return render(request, 'core/forget_password.html')

def password_reset(request):
    return render(request, 'core/password_reset.html')


def change_password(request):
    return render(request, 'core/change_password.html')
    

def sign_up_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('sign_in')
    else:
        form = SignUpForm()
    return render(request, 'core/sign_up.html', {'form': form})