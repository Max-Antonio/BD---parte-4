from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Administrador, Editora, Livro, Leitor, Livros_Leitor
from .serializers import AdministradorSerializer, EditoraSerializer, LivroSerializer, LeitorSerializer, Livros_LeitorSerializer

def administrador_list(request):
    administradores = Administrador.objects.all()
    serializer = AdministradorSerializer(administradores, many=True)
    return JsonResponse(serializer.data, safe=False)

def editora_list(request):
    editoras = Editora.objects.all()
    serializer = EditoraSerializer(editoras, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET', 'POST'])
def livro_list(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        serializer = LivroSerializer(livros, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = LivroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def leitor_list(request):
    if request.method == 'GET':
        leitores = Leitor.objects.all()
        serializer = LeitorSerializer(leitores, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = LeitorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

def livros_leitor_list(request):
    livros_leitores = Livros_Leitor.objects.all()
    serializer = Livros_LeitorSerializer(livros_leitores, many=True)
    return JsonResponse(serializer.data, safe=False)