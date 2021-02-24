from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from API.models import Carro

# Create your views here.

def index(request):
    response = {}
    return JsonResponse(response, json_dumps_params={'indent': 2})

def get_carro(request, carro_nombre):
    if request.method == 'GET':
        try:
            carro = Carro.objects.get(nombre=carro_nombre)
            response = {'Carro': carro.nombre, 'Color': carro.color, 'Velocidad Maxima': carro.velocidad_maxima}
        except:
            response = json.dumps([{ 'Error': 'Ningun carro con ese nombre' }])
    return JsonResponse(response, json_dumps_params={'indent': 2})

@csrf_exempt
def add_carro(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        carro_nombre = payload['carro_nombre']
        carro_color = payload['carro_color']
        velocidad_maxima = payload['velocidad_maxima']
        carro = Carro(nombre=carro_nombre, color=carro_color, velocidad_maxima=velocidad_maxima)
        try:
            carro.save()
            response = json.dumps([{'Exito': 'Carro agregado'}])
        except:
            response = json.dumps([{'Error': 'Carro no agregado'}])
    return HttpResponse(response, content_type='text/json')