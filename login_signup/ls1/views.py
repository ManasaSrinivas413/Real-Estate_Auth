
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from .models import superuser
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful! Please login.")
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try:
                user = superuser.objects.get(username=username, password=password)
                messages.success(request, f"Welcome {user.username}! You are logged in as {user.role}.")
            except superuser.DoesNotExist:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
