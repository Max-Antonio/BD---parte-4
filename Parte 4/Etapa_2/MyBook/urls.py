"""
URL configuration for MyBook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyBook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administradores/', views.administrador_list),
    path('editoras/', views.editora_list),
    path('livros/', views.livro_list),
    path('livros/<int:isbn>', views.livro_detalhe),
    path('leitores/', views.leitor_list),
    path('leitores/<str:cpf>', views.leitor_detalhe),
    path('livros_leitores/', views.livros_leitor_list),
    path('livros_leitores/<int:id>', views.livros_leitor_detalhe),
]
