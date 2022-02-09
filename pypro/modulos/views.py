from django.shortcuts import render
from pypro.modulos import facade


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulos_detalhes.html', {'modulo': modulo, 'aulas':aulas})
