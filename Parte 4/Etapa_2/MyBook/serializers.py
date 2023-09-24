from rest_framework import serializers
from .models import Administrador, Editora, Livro, Leitor, Livros_Leitor

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leitor
        fields = '__all__'

class Livros_LeitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livros_Leitor
        fields = '__all__'