from django.contrib import admin
from .models import *

admin.site.register(Categoria)
admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'criado_em', 'status')
    list_filter = ('status', 'criado_em', 'autor', 'categoria')
    search_fields = ('titulo', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'criado_em'

admin.site.register(Post, PostAdmin)