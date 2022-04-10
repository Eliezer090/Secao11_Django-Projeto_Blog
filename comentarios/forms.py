from django.forms import ModelForm
from .models import Comentario, Post


class FormComentario(ModelForm):
    def clean(self):
        # Validando formulário de models.py
        super().clean()
        # Validando Nome
        nome = self.cleaned_data.get('nome_comentario')
        if len(nome) < 3:
            self.add_error('nome_comentario', 'Nome muito curto')
        # Validando Comentário
        comentario = self.cleaned_data.get('comentario')
        if len(comentario) < 5:
            self.add_error('comentario', 'Comentário muito curto')

    class Meta:
        model = Comentario
        # Os fields vem do models.py
        fields = ['nome_comentario', 'email_comentario', 'comentario']
