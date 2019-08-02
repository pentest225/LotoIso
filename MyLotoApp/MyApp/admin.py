from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Admin Page Super Plus "
admin.site.site_title = "Admin "
admin.site.index_title = "Bienvenue sur la page d'administration ;)"

admin.site.register(Profile)
#@admin.register(Client)
# class ClientAdmin (admin.ModelAdmin):
#     # list_display = ('username' ,'email','numero','compte',)
#     # list_filter = ("username","numero")
#     # search_fields = ('username' ,'numero',)
#     # list_per_page = 50
#     # ordering = ['username',]

@admin.register(Equipe)
class EquipeAdmin (admin.ModelAdmin):
    list_display = ('nom' ,'logo','cote',)
    list_filter = ("nom",)
    search_fields = ('nom' ,)
    list_per_page = 500
    ordering = ['nom',]


@admin.register(Sport)
class SportAdmin (admin.ModelAdmin):
    list_display = ('nom' ,'logo','date_add',)
    list_filter = ("nom",'date_add',)
    search_fields = ('nom' ,'date_add',)
    list_per_page = 10
    ordering = ['nom','date_add',]


@admin.register(Math)
class MathAdmin (admin.ModelAdmin):
    list_display = ('typeSport','date_math' ,'heure_debut','heure_fin','idEquipe1','idEquipe2','scoreEq1','scoreEq2')
    list_filter = ("idEquipe1","idEquipe2",)
    search_fields = ('idEquipe1','idEquipe2',)
    list_per_page = 500
    ordering = ['idEquipe1','idEquipe2',]


@admin.register(Parier)
class ParierAdmin (admin.ModelAdmin):
    list_display = ('idUser','idMath' ,'date_parie','mise','gainParie','idVictoir')
    list_filter = ("idUser","date_parie","gainParie","idMath",)
    search_fields = ("idUser","date_parie","gainParie","idMath",)
    list_per_page = 500
    ordering = ['date_parie','gainParie',]