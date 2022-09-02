from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familia

def familiares(request):
    familiar1 = Familia.objects.create(nombre = "Marcelo", anio = 52 , fecha_nac = "1970-10-7")
    familiar2 = Familia.objects.create(nombre = "Marisa", anio = 54 , fecha_nac = "1968-04-20")
    familiar3 = Familia.objects.create(nombre = "Matias", anio = 33 , fecha_nac = "1989-12-04")
    
    familiar1.save()
    familiar2.save()
    familiar3.save()


    family_list=[familiar1, familiar2, familiar3]
    diccionario={"list":family_list}

    plantilla=loader.get_template("template.html")
    doc=plantilla.render(diccionario)


    return HttpResponse(doc)