from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from httpx import request
from .forms import RegisterForm
from django.contrib.auth.models import Group

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)

                next_url = request.GET.get('next')

                if next_url:
                    return redirect(next_url)

                return redirect('landing_page')
            
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    
    return redirect('landing_page')

def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()

            grupo = Group.objects.get(name="autores")
            user.groups.add(grupo)

            login(request, user)
            
            return redirect('landing_page')

    return render(request, 'accounts/register.html', {'form': form})