from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout  # Import the logout function
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import logout

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                password=form.cleaned_data['senha'],
            ) 
            register = form.save(commit=False)
            register.user = user
            register.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            register = Register.objects.get(user=user)
            context = {
                'entidade': register.entidade,
                'email': register.email,
            }
        except Register.DoesNotExist:
            context = {
                'error_message': 'No additional user information found.',
            }
        return render(request, 'login/logado.html', context)

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                return redirect('success')
            else:
                return render(request, 'login/login.html', {'form': form, 'error_message': 'Usuário ou senha inválidos.'})
    else:
        form = LoginForm()

    return render(request, 'login/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def login_success(request):
    user = request.user
    try:
        register = Register.objects.get(user=user)
        context = {
            'entidade': register.entidade,
            'email': register.email,
        }
    except Register.DoesNotExist:
        context = {
            'error_message': 'Sem informação adicionais encontradas.',
        }
    return render(request, 'login/success.html', context)

@login_required
def update_user(request):
    user = request.user
    register, created = Register.objects.get_or_create(user=user)
    success = False
    
    if request.method == 'POST':
        form = RegisterForm(request.POST, instance=register)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = RegisterForm(instance=register)
    
    return render(request, 'login/update.html', {'form': form, 'success': success})

@login_required
def delete_user(request):
    user = request.user
    try:
        register = Register.objects.get(user=user)
        register.delete()
    except Register.DoesNotExist:
        pass
    user.delete()
    return redirect('index')