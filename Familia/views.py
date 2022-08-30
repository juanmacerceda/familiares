from argparse import _MutuallyExclusiveGroup
from django.shortcuts import render
from re import template
from django.http import HttpResponse
from django.template import Template, loader
from AppFamilia.models import Hermano

def home(request):
    nom_ape="Ingrid"
    edad=int(60)
    diccionario={'nombre': nom_ape, 'edad': edad}
    plantilla=loader.get_template('template.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def madre(request):
    nom_ape="Ingrid"
    edad=int(60)
    diccionario={'nombre': nom_ape, 'edad': edad}
    plantilla=loader.get_template('madre.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

def hermano(request):
    hermano=Hermano(nombre="Mauro", apellido="Tomas", edad=int(40), email="mauro.tomas@gmail.com")
    hermano.save()
    texto=f"{hermano.nombre} {hermano.apellido}, {hermano.edad} años,{hermano.email}"
    return HttpResponse(texto)
    
def padre(request):
    nombre= "Sergio Cerceda"
    edad=int(60)
    dni= "27.540.862"
    Nacionalidad= "Argentino"
    return HttpResponse(f"Mi padre se llama {nombre}, tiene {edad} años, DNI:{dni}")


