from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from .models import Post
from django.db.models import Count, Q,Case,When

class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-data_post').filter(publicado_post=True)
        qs = qs.annotate(numero_comentarios=Count(Case(
            When(comentario__publicado_comentario=True, then=1))))
        return qs




class PostBusca(PostIndex):
    template_name = 'posts/post_busca.html'

    def get_queryset(self):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo',None)
        if termo:
            qs = qs.filter(
                Q(titulo_post__icontains=termo) |
                Q(conteudo_post__icontains=termo) |
                Q(excerto_post__icontains=termo)|
                Q(autor_post__username__icontains=termo)         
            )        
        return qs


class PostCategoria(PostIndex):
    template_name = 'posts/post_categoria.html'

    def get_queryset(self):
        #o que foi feito no get_queryset da classe pai, está implementado aqui também
        qs = super().get_queryset()
        """O filtro abaixo é o seguinte
            categoria_post é uma fk do posts(post.models)
            nome_cat é o nome da categoria(categorias.models)
            iexact é o tipo de filtro que querro fazer e ele é case sensitive
        """
        qs = qs.filter(categoria_post__nome_cat__iexact=self.kwargs.get('categoria',None))

        return qs


class PostDetalhes(UpdateView):
    pass
