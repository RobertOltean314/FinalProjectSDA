from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Profile
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not Profile.objects.filter(user=user).exists():
                Profile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'users/logout.html')
