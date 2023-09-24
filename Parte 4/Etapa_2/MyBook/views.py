from django.http import JsonResponse
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

def livro_list(request):
    livros = Livro.objects.all()
    serializer = LivroSerializer(livros, many=True)
    return JsonResponse(serializer.data, safe=False)

def leitor_list(request):
    leitores = Leitor.objects.all()
    serializer = LeitorSerializer(leitores, many=True)
    return JsonResponse(serializer.data, safe=False)

def livros_leitor_list(request):
    livros_leitores = Livros_Leitor.objects.all()
    serializer = Livros_LeitorSerializer(livros_leitores, many=True)
    return JsonResponse(serializer.data, safe=False)