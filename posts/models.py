from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo_post = models.CharField(max_length=100, verbose_name='Título')
    autor_post = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, verbose_name='Autor')
    data_post = models.DateTimeField(default=timezone.now, verbose_name='Data')
    conteudo_post = models.TextField(verbose_name='Conteúdo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(
        Categoria, on_delete=models.DO_NOTHING, null=True, blank=True, verbose_name='Categoria')
    imagem_post = models.ImageField(
        upload_to='posts_img/%Y/%m/%d', null=True, blank=True, verbose_name='Imagem')
    publicado_post = models.BooleanField(
        default=False, verbose_name='Publicado')

    def __str__(self):
        return self.titulo_post