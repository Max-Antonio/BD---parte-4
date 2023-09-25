from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Administrador, Editora, Livro, Leitor, Livros_Leitor
from .serializers import AdministradorSerializer, EditoraSerializer, LivroSerializer, LeitorSerializer, Livros_LeitorSerializer

@api_view(['GET', 'POST'])
def administrador_list(request):
    if request.method == 'GET':
        administradores = Administrador.objects.all()
        serializer = AdministradorSerializer(administradores, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = AdministradorSerializer(data=request.data)
        if serializer.is_valis():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def editora_list(request):
    if request.method == 'GET':
        editoras = Editora.objects.all()
        serializer = EditoraSerializer(editoras, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        serializer = EditoraSerializer(data=request.data)
        if serializer.is_valis():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)   

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

@api_view(['PUT', 'DELETE', 'GET'])
def livro_detalhe(request, isbn):
    try:
        livro = Livro.objects.get(pk=isbn)
    except Livro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        serializer = LivroSerializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return Response(serializer.data)
    
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

@api_view(['GET', 'PUT', 'DELETE'])
def leitor_detalhe(request, cpf):
    try:
        leitor = Leitor.objects.get(pk=cpf)
    except Leitor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LeitorSerializer(leitor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        leitor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = LeitorSerializer(leitor)
        return Response(serializer.data)
    
def livros_leitor_list(request):
    livros_leitores = Livros_Leitor.objects.all()
    serializer = Livros_LeitorSerializer(livros_leitores, many=True)
    return JsonResponse(serializer.data, safe=False)