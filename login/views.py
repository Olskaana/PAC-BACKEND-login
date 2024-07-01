from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth import logout
from .serializer import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.http import JsonResponse
import json
from django.views.decorators.http import require_POST

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

class RegisterView(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            serializer = RegisterSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            
            return JsonResponse(serializer.errors, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
@csrf_exempt
@require_POST
def login_view(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        senha = data.get('senha')
        entidade = data.get('entidade')

        user = authenticate(request, username=email, password=senha, entidade=entidade)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error_message': 'Invalid credentials'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error_message': 'Invalid JSON'}, status=400)


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
            'error_message': 'No additional user information found.',
        }
    return JsonResponse(context)

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

    return JsonResponse({'success': success})

@login_required
def delete_user(request):
    user = request.user
    try:
        register = Register.objects.get(user=user)
        register.delete()
    except Register.DoesNotExist:
        pass
    user.delete()
    return JsonResponse({'message': 'User deleted successfully'})