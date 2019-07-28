from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Admin Page Super Plus "
admin.site.site_title = "Admin "
admin.site.index_title = "Bienvenue sur la page d'administration ;)"

admin.site.register(Client)
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
    list_per_page = 10
    ordering = ['nom',]


@admin.register(Sport)
class SportAdmin (admin.ModelAdmin):
    list_display = ('Nom' ,'logo',)
    list_filter = ("Nom",)
    search_fields = ('Nom' ,)
    list_per_page = 10
    ordering = ['Nom',]


@admin.register(Math)
class MathAdmin (admin.ModelAdmin):
    list_display = ('date_debut' ,'date_fin','id_equip1','id_equip2','scoreEq1','scoreEq2')
    list_filter = ("id_equip1","id_equip2",)
    search_fields = ('id_equip1','id_equip2',)
    list_per_page = 50
    ordering = ['id_equip1','id_equip2',]