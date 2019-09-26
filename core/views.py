from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import *

def login_view(request):
    if request.user.is_authenticated:
        return redirect('core:profile')
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('core:profile')
    return render(request, 'login.html', {'form': form, 'title': 'Sign In'})

def logout_view(request):
    logout(request)
    return redirect('core:login')

def signup_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        raw_pass = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_pass)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('core:profile')
    return render(request, 'signup.html', {'form': form, 'title': 'Sign Up'})

def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('core:login')
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('core:profile')
    form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form, 'title': 'Update Profile'})