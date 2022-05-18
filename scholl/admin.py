from django.contrib import admin
from scholl.models import Aluno

class Alunos(admin.ModelAdmin):
    list_display = ('name', 'rg')
    list_display_links = ('name', 'rg')
    search_fields = ('name',)

admin.site.register(Aluno, Alunos)
