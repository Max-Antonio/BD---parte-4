from django.db import models 

class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True, null=False) #chave primária, auto-incremental, não nulo

class Editora(models.Model):
    id_editora = models.AutoField(primary_key=True, null=False) #chave primária, auto-incremental, não nulo
    nome = models.CharField(null=False, max_length=45) #não nulo


class Livro(models.Model):
    ISBN = models.CharField(primary_key=True, null=False, max_length=13) #chave primária, não nulo
    nome = models.CharField(null=False, max_length=50) #não nulo
    quantidade_leitores = models.IntegerField(null=False) #não nulo
    existe_no_sistema = models.BooleanField(null=False) #não nulo
    id_editora = models.ForeignKey(Editora, on_delete=models.CASCADE) #chave estrangeira, ao deletar a editora deleta todos os livros associados a ela
    id_admnistrador = models.ForeignKey(Administrador, on_delete=models.SET(-1)) #chave estrangeira, eu deletar administrador seta valor para -1

class Leitor(models.Model):
    cpf = models.CharField(primary_key=True, null=False, max_length=11) #chave primária, não nulo
    primeiro_nome = models.CharField(null=False, max_length=20) #não nulo
    segundo_nome = models.CharField(max_length=20)
    email = models.CharField(null=False, max_length=45) #não nulo
    senha = models.CharField(null=False, max_length=45) #não nulo
    apelido = models.CharField(null=False, max_length=45) #não nulo

class Livros_Leitor(models.Model):
    cpf = models.ForeignKey(Leitor, on_delete=models.CASCADE) #chave estrangeira, chave primária
    ISBN = models.ForeignKey(Livro, on_delete=models.CASCADE) #chave estrangeira, chave primária
    livro_lido = models.CharField(max_length=45)
    livro_favorito = models.CharField(max_length=45)
    livro_em_progresso = models.CharField(max_length=45)
    livro_pretende_ler = models.CharField(max_length=45)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['cpf', 'ISBN'], name="cpf_e_ISBN"
            )
        ]
