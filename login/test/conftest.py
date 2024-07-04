import pytest
from django.contrib.auth.models import User
from login.models import Register

@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        if 'username' not in kwargs:
            kwargs['username'] = kwargs['email']
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def create_register(db, create_user):
    def make_register(**kwargs):
        user_kwargs = kwargs.pop('user_kwargs', {})
        user = create_user(**user_kwargs)
        return Register.objects.create(user=user, **kwargs)
    return make_register