# login/serializer.py

from rest_framework import serializers
from .models import Register
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['entidade', 'email', 'senha']

    def create(self, validated_data):
        email = validated_data['email']
        senha = validated_data['senha']
        entidade = validated_data['entidade']
    
        user = User.objects.create_user(username=email, email=email, password=senha)
        
        register_instance = Register.objects.create(user=user, entidade=entidade, email=email, senha=senha)
        
        return register_instance
