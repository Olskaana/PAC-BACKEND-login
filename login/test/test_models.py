# login/tests/test_models.py

import pytest
from django.contrib.auth.models import User
from login.models import Register

@pytest.mark.django_db
def test_register_creation(create_user):
    user = create_user(email='test@example.com', password='password123', username='testuser')
    register = Register.objects.create(user=user, entidade='Test Entidade', email='test@example.com', senha='password123', municipio='Jaraguá do Sul')
    assert register.email == 'test@example.com'
    assert register.entidade == 'Test Entidade'
    assert register.municipio == 'Jaraguá do Sul'

@pytest.mark.django_db
def test_register_unique_email(create_user):
    user1 = create_user(email='test1@example.com', password='password123', username='testuser1')
    Register.objects.create(user=user1, entidade='Test Entidade', email='test1@example.com', senha='password123', municipio='Jaraguá do Sul')

   
