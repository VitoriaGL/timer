from django.contrib import admin
from .models import Contador


@admin.register(Contador)
class ContadorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'valor', 'criado_em', 'atualizado_em']
    list_filter = ['criado_em']
    search_fields = ['nome']

