from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import PlanoForm, TopicoForm, AdicionalForm, AcaoForm, BibliotecaForm
from .models import Plano, Topico, Adicional, Acao, Biblioteca
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from .serializer import (
    PlanoSerializer, TopicoSerializer, AdicionalSerializer,
    AcaoSerializer, BibliotecaSerializer
)

class MunicipioAPIView(APIView):
    def get(self, request, municipio):
        planos = Plano.objects.filter(municipio=municipio)
        serializer = PlanoSerializer(planos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PlanoDetailAPIView(APIView):
    def get(self, request, municipio, id_plano):
        plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)
        serializer = PlanoSerializer(plano)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, municipio, id_plano):
        plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)
        plano.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CriarPlanoAPIView(APIView):
    def post(self, request, municipio):
        data = request.data
        data['municipio'] = municipio
        serializer_plano = PlanoSerializer(data=data)
        if serializer_plano.is_valid():
            plano = serializer_plano.save()
            serializer_topicos = TopicoSerializer(data=data.get('topicos', []), many=True)
            serializer_adicionais = AdicionalSerializer(data=data.get('adicionais', []), many=True)
            serializer_acoes = AcaoSerializer(data=data.get('acoes', []), many=True)
            serializer_bibliotecas = BibliotecaSerializer(data=data.get('bibliotecas', []), many=True)

            if (serializer_topicos.is_valid() and serializer_adicionais.is_valid() 
                and serializer_acoes.is_valid() and serializer_bibliotecas.is_valid()):
                
                for topico_data in serializer_topicos.validated_data:
                    Topico.objects.create(plano=plano, **topico_data)
                
                for adicional_data in serializer_adicionais.validated_data:
                    Adicional.objects.create(plano=plano, **adicional_data)
                
                for acao_data in serializer_acoes.validated_data:
                    Acao.objects.create(plano=plano, **acao_data)
                
                for biblioteca_data in serializer_bibliotecas.validated_data:
                    Biblioteca.objects.create(plano=plano, **biblioteca_data)
                
                return Response({'message': 'Plano criado com sucesso.'}, status=status.HTTP_201_CREATED)

            return Response({
                'errors': {
                    'topicos': serializer_topicos.errors,
                    'adicionais': serializer_adicionais.errors,
                    'acoes': serializer_acoes.errors,
                    'bibliotecas': serializer_bibliotecas.errors,
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer_plano.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EditarPlanoAPIView(APIView):
    def put(self, request, municipio, id_plano):
        plano = get_object_or_404(Plano, id=id_plano, municipio=municipio)
        serializer_plano = PlanoSerializer(plano, data=request.data)
        if serializer_plano.is_valid():
            plano = serializer_plano.save()

            serializer_topicos = TopicoSerializer(data=request.data.get('topicos'), many=True)
            serializer_adicionais = AdicionalSerializer(data=request.data.get('adicionais'), many=True)
            serializer_acoes = AcaoSerializer(data=request.data.get('acoes'), many=True)
            serializer_bibliotecas = BibliotecaSerializer(data=request.data.get('bibliotecas'), many=True)

            if (serializer_topicos.is_valid() and serializer_adicionais.is_valid() 
                and serializer_acoes.is_valid() and serializer_bibliotecas.is_valid()):
                
                Topico.objects.filter(plano=plano).delete()
                Adicional.objects.filter(plano=plano).delete()
                Acao.objects.filter(plano=plano).delete()
                Biblioteca.objects.filter(plano=plano).delete()

                for topico_data in serializer_topicos.validated_data:
                    Topico.objects.create(plano=plano, **topico_data)
                
                for adicional_data in serializer_adicionais.validated_data:
                    Adicional.objects.create(plano=plano, **adicional_data)
                
                for acao_data in serializer_acoes.validated_data:
                    Acao.objects.create(plano=plano, **acao_data)
                
                for biblioteca_data in serializer_bibliotecas.validated_data:
                    Biblioteca.objects.create(plano=plano, **biblioteca_data)
                
                return Response({'message': 'Plano atualizado com sucesso.'}, status=status.HTTP_200_OK)

            return Response({
                'errors': {
                    'topicos': serializer_topicos.errors,
                    'adicionais': serializer_adicionais.errors,
                    'acoes': serializer_acoes.errors,
                    'bibliotecas': serializer_bibliotecas.errors,
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer_plano.errors, status=status.HTTP_400_BAD_REQUEST)