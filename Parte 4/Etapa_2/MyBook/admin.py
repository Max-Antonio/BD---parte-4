from django.contrib import admin
from .models import Administrador, Editora, Livro, Leitor, Livros_Leitor

admin.site.register(Administrador)
admin.site.register(Editora)
admin.site.register(Livro)
admin.site.register(Leitor)
admin.site.register(Livros_Leitor)