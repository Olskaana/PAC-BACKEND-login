# login/tests/test_views.py

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from login.models import Register
from login.forms import RegisterForm, LoginForm
import uuid

@pytest.mark.django_db
def test_register_view(client):
    unique_suffix = uuid.uuid4()
    unique_email = f'test_{unique_suffix}@example.com'
    unique_username = f'testuser_{unique_suffix}'

    data = {
        'entidade': 'Test Entidade',
        'email': unique_email,
        'senha': 'password123',
        'confirmar_senha': 'password123',
        'municipio': 'Jaraguá do Sul',
        'username': unique_username  # Assuming your form/view uses a username field
    }

    response = client.post(reverse('register'), data)
    assert response.status_code == 302  # Or the expected status code
    assert User.objects.filter(username=unique_username).exists()
    
@pytest.mark.django_db
def test_login_view_authenticated(client, create_user):
    user = create_user(email='test@example.com', password='password123')
    Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    client.login(username='test@example.com', password='password123')
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'entidade' in response.context
    assert response.context['entidade'] == 'Test Entidade'

@pytest.mark.django_db
def test_login_view(client, create_user):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], LoginForm)
    
    user = create_user(email='test@example.com', password='password123')
    Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    
    data = {
        'email': 'test@example.com',
        'senha': 'password123',
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert response.url == reverse('success')

@pytest.mark.django_db
def test_logout_view(client, create_user):
    user = create_user(email='test@example.com', password='password123')
    client.login(username='test@example.com', password='password123')
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url == reverse('index')

@pytest.mark.django_db
def test_login_success_view(client, create_user):
    user = create_user(email='test@example.com', password='password123')
    Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    client.login(username='test@example.com', password='password123')
    url = reverse('success')
    response = client.get(url)
    assert response.status_code == 200
    assert 'entidade' in response.context
    assert response.context['entidade'] == 'Test Entidade'

@pytest.mark.django_db
def test_update_user_view(client, create_user):
    user = create_user(email='test@example.com', password='password123')
    register = Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    client.login(username='test@example.com', password='password123')
    url = reverse('update_user')
    response = client.get(url)
    assert response.status_code == 200
    assert isinstance(response.context['form'], RegisterForm)
    
    data = {
        'entidade': 'Updated Entidade',
        'email': 'updated@example.com',
        'senha': 'password123',
        'confirmar_senha': 'password123',
        'municipio': 'Jaraguá do Sul'
    }
    response = client.post(url, data)
    assert response.status_code == 200
    register.refresh_from_db()
    assert register.entidade == 'Updated Entidade'
    assert register.email == 'updated@example.com'

@pytest.mark.django_db
def test_delete_user_view(client, create_user):
    user = create_user(email='test@example.com', password='password123')
    Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    client.login(username='test@example.com', password='password123')
    url = reverse('delete_user')
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse('index')
    assert not User.objects.filter(username='test@example.com').exists()
    assert not Register.objects.filter(email='test@example.com').exists()
