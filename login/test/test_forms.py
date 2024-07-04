# login/tests/test_forms.py

import pytest
from django.contrib.auth.models import User
from login.forms import RegisterForm, LoginForm
from login.models import Register

@pytest.mark.django_db
def test_register_form_valid():
    form_data = {
        'entidade': 'Test Entidade',
        'email': 'test@example.com',
        'senha': 'password123',
        'confirmar_senha': 'password123',
        'municipio': 'Jaraguá do Sul'
    }
    form = RegisterForm(data=form_data)
    assert form.is_valid()
    user = form.save()
    assert User.objects.filter(email='test@example.com').exists()

@pytest.mark.django_db
def test_register_form_duplicate_email(create_user):
    create_user(email='test@example.com', password='password123', username='testuser')
    form_data = {
        'entidade': 'Test Entidade',
        'email': 'test@example.com',
        'senha': 'password123',
        'confirmar_senha': 'password123',
        'municipio': 'Jaraguá do Sul'
    }
    form = RegisterForm(data=form_data)
    assert not form.is_valid()

@pytest.mark.django_db
def test_login_form_valid():
    user = User.objects.create_user(email='test@example.com', password='password123', username='testuser')
    Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')

    form_data = {
        'email': 'test@example.com',
        'senha': 'password123',
        'entidade': 'Test Entidade'
    }
    form = LoginForm(data=form_data)
    assert form.is_valid()

@pytest.mark.django_db
def test_login_form_invalid():
    form_data = {
        'email': 'nonexistent@example.com',
        'senha': 'wrongpassword',
        'entidade': 'Test Entidade'
    }
    form = LoginForm(data=form_data)
    assert not form.is_valid()
