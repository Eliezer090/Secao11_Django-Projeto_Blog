from django.contrib import admin

from comentarios.models import Comentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome_comentario', 'email_comentario', 'post_comentario', 'data_comentario', 'publicado_comentario')
    list_filter = ('publicado_comentario',)
    list_editable = ('publicado_comentario',)
    list_display_links = ('nome_comentario','email_comentario')    

admin.site.register(Comentario, ComentarioAdmin)
