from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password'] 
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('success')
                else:
                    form.add_error(None, "Email ou senha incorretos.")
            except User.DoesNotExist:
                form.add_error(None, "Usuário não encontrado.")
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

@login_required
def login_success(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'is_staff': user.is_staff,
    }
    return render(request, 'success.html', context)